from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.stock_model import Stock
from schema.stock_schema import StockSchema
from commons.authentication import jwt_required_decorator
from fastapi.security import OAuth2PasswordBearer
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# GET ALL STOCK
@router.get("/stocks",response_model=list[StockSchema])
def get_all_stock(db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    stock=db.query(Stock).all()
    return stock

# GET STOCK BY TICKER
@router.get("/stock/{ticker}",response_model=StockSchema)
def get_stock_by_ticker(ticker:str,db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    stock=db.query(Stock).filter(Stock.ticker==ticker).first()
    if stock is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stock not found")
    return stock

# GET STOCK BY ID
@router.get("/stock/{stock_id}",response_model=StockSchema)
def get_stock_by_ticker(stock_id:int,db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    stock=db.query(Stock).filter(Stock.id==stock_id).first()
    if stock is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stock not found")
    return stock

# CREATE NEW STOCK
@router.post("/user/add",response_model=StockSchema)
def create_new_stock(stock=StockSchema,db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    new_stock=Stock(
        ticker=stock.ticker,
        price=stock.price,
    )
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

