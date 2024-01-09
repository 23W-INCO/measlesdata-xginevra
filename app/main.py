from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
import sqlite3
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()


# Endpoint to serve the HTML file
@app.get("/")
def get_html():
    return FileResponse("./index.html")


# Serve static files (HTML, JS, CSS)
# app.mount("/", StaticFiles(directory="./", html=True), name="static")
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///data_for_web_application.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
#
# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
#
# database = Database("sqlite:///data_for_web_application.db")
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://127.0.0.1:8000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/data")
async def get_data():
    # Replace 'your_database_file.db' with your actual database file
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM measles_data"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data


# @app.post("/data")
# async def fetch_data(id: int):
#     query = f"SELECT * FROM measles_data WHERE id ={id}"
#     results = await database.fetch_all(query=query)
#
#     return results



# @app.on_event("startup")
# async def database_connect():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def database_disconnect():
#     await database.disconnect()
