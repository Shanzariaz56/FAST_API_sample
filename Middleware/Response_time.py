import time
from fastapi import FastAPI, Request

# Function to add process time header as middleware
def add_process_time_header(app: FastAPI):
    @app.middleware("http")
    async def middleware(request: Request, call_next):
        start_time = time.perf_counter()  # Start timing
        response = await call_next(request)  # Process the request
        process_time = time.perf_counter() - start_time  # Calculate the time taken
        response.headers["X-Process-Time"] = str(process_time)  # Add header
        return response
