from fastapi import FastAPI
from fastapi.responses import FileResponse
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Endpoint to serve the HTML file
@app.get("/")
def get_html():
    return FileResponse("./index.html")


# Serve static files (HTML, JS, CSS)
# app.mount("/", StaticFiles(directory="./", html=True), name="static")


@app.get("/data")
async def get_data():
    # do this for every visualisation that requires parts of the data
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM measles_data"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data


@app.get("/measlesdata1")
async def get_data1():
    # do this for every visualisation that requires parts of the data
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = '''
        SELECT *
        FROM measles_data
        WHERE location IN (
            'baden-wuerttemberg', 'bayern', 'berlin', 'brandenburg', 'bremen',
            'hamburg', 'hessen', 'mecklenburg-vorpommern', 'niedersachsen',
            'nordrhein-westfalen', 'rheinland-pfalz', 'saarland', 'sachsen',
            'sachsen-anhalt', 'schleswig-holstein', 'thueringen'
        )
        AND population <> 'N.A'
        AND cases <> 'N.A'
        AND vaccination_rate <> 'N.A'
        AND cases_100000 <> 'N.A';
    '''

    cursor.execute(query)
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    data_list = []
    for items in data:
        data_dict = {}
        data_dict["location"] = items[1]
        data_dict["population"] = items[2]
        data_dict["cases"] = items[3]
        data_dict["vaccination_rate"] = items[4]
        data_dict["cases_100000"] = items[5]

        data_list.append(data_dict)
    return data_list


@app.get("/cities")
async def get_data2():
    # do this for every visualisation that requires parts of the data
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = '''
        SELECT *
        FROM measles_data
        WHERE vaccination_rate = 'N.A'
        AND cases_100000 = 'N.A';
    '''

    cursor.execute(query)
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    data_list = []
    for items in data:
        data_dict = {}
        data_dict["location"] = items[1]
        data_dict["population"] = items[2]
        data_dict["cases"] = items[3]

        data_list.append(data_dict)
    return data_list
