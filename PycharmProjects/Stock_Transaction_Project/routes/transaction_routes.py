from fastapi import APIRouter, status,Depends,HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.transaction_model import Transaction
from models.stock_model import Stock
from models.user_model import User
from sqlalchemy.types import DECIMAL
from schema.transaction_schema import TransactionSchema,TransactionType
from commons.authentication import jwt_required_decorator
from fastapi.security import OAuth2PasswordBearer
router=APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# GET ALL TRANSACTION
@router.get("/transactions",response_model=list[TransactionSchema])
def get_all_transactions(db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    transactions=db.query(Transaction).all()
    return transactions

# CREATE NEW TRANSACTION
@router.post("/transaction/add", response_model=TransactionSchema)
def add_new_transaction(transaction: TransactionSchema, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    """
    Create a new transaction. The user must be authenticated via JWT.
    """
    # Extract transaction details
    user_id = transaction.user_id
    stock_id = transaction.stock_id
    transaction_type = transaction.transaction_type
    transaction_volume = transaction.transaction_volume

    # Check if user and stock exist
    user_instance = db.query(User).filter(User.id == user_id).first()
    stock_instance = db.query(Stock).filter(Stock.id == stock_id).first()

    if user_instance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    if stock_instance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stock not found.")

    # Calculate transaction price
    transaction_price = stock_instance.price * DECIMAL(transaction_volume)

    # Validate transaction
    if transaction_type == TransactionType.BUY:
        if user_instance.initial_balance < transaction_price:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient balance.")
        user_instance.initial_balance -= transaction_price
    elif transaction_type == TransactionType.SELL:
        user_instance.initial_balance += transaction_price
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid transaction type.")

    # Save changes to the user balance
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)

    # Create the transaction
    new_transaction = Transaction(
        user_id=user_id,
        stock_id=stock_id,
        transaction_type=transaction_type,
        transaction_volume=transaction_volume,
        transaction_price=transaction_price
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction
