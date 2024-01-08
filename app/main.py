from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table

DATABASE_URL = "sqlite:///data_for_web_application.db"

metadata = MetaData()

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

table = Table(
    "measles_data",
    metadata,
    sqlalchemy.Column("location", sqlalchemy.String),
    sqlalchemy.Column("cases_100000", sqlalchemy.Float),
    sqlalchemy.Column("vaccination_rate", sqlalchemy.Float),
)

app = FastAPI()

# Allow all origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, JS, CSS)
app.mount("/", StaticFiles(directory="./", html=True), name="static")


# Endpoint to serve the HTML file
@app.get("/")
def get_html():
    return FileResponse("./index.html")


# Endpoint to fetch data
@app.get("/data")
async def get_data():
    query = table.select()
    data = await database.fetch_all(query)
    return data

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app with uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
