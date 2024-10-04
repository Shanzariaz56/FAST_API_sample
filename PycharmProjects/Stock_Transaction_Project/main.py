from fastapi import FastAPI
from routes.transaction_routes import router as transaction_router
from routes.user_routes import router as user_router
from routes.stock_routes import router as stock_router
from routes.user_auth_routes import router as user_auth_router

app = FastAPI()

# Include routers
app.include_router(user_auth_router)
app.include_router(transaction_router)
app.include_router(user_router)
app.include_router(stock_router)
