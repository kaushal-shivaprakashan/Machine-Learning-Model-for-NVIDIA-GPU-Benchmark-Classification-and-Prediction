from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import pandas as pd

# FastAPI app
app = FastAPI()

# Database connection utility
def get_db_connection():
    db_path = "gpu_benchmark.db"  # Path to the SQLite database
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Enables fetching rows as dictionaries
    return conn

# Endpoint for root
@app.get("/")
def read_root():
    return {"message": "Welcome to the GPU Benchmarks API!"}

# Pydantic model for GPU input
class GPURequest(BaseModel):
    gpu_name: str

# Fetch GPU performance by GPU name
@app.post("/gpu/")
def get_gpu_performance(data: GPURequest):
    conn = get_db_connection()
    query = "SELECT * FROM GPU_Performance WHERE GPU_Name = ?"
    gpu = conn.execute(query, (data.gpu_name,)).fetchone()
    conn.close()

    if not gpu:
        raise HTTPException(status_code=404, detail="GPU not found")
    
    return dict(gpu)

# Endpoint to fetch all GPU data
@app.get("/gpus/")
def get_all_gpus():
    conn = get_db_connection()
    query = "SELECT * FROM GPU_Performance"
    gpus = conn.execute(query).fetchall()
    conn.close()

    return [dict(row) for row in gpus]
