from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
import sqlite3

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, JS, CSS)
app.mount("/", StaticFiles(directory="./", html=True), name="static")

# Connect to SQLite database
database_url = "sqlite:///data_for_web_application.db"
database = Database(database_url)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Endpoint to serve the HTML file
@app.get("/")
def get_html():
    return FileResponse("./index.html")


# Endpoint to fetch data from the SQLite database
@app.get("/data")
async def get_data():
    query = "SELECT * FROM measles_data"
    data = await database.fetch_all(query)
    return data


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app with uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
