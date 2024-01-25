from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from jsonindb import JsonInDatabaseTranformer


# use the following command: python3 -m uvicorn main:app --reload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

json_in_db = JsonInDatabaseTranformer()
json_in_db.push_json_data_in_fresh_db("measles_statistics_fhir.json")


# Endpoint to serve the HTML file
@app.get("/")
def get_html():
    return FileResponse("./index.html")


# Serve static files (HTML, JS, CSS)


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
            'Baden-Wuerttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thueringen'
        )
        OR ( population <> 'N.A'
        AND cases <> 'N.A'
        AND vaccination_rate <> 'N.A'
        AND cases_100000 <> 'N.A');
        
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
        WHERE location NOT IN (
            'Baden-Wuerttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thueringen'
        )
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


@app.get("/citiesupto200000")
async def get_data2():
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = '''
        SELECT *
        FROM measles_data
        WHERE location NOT IN (
            'Baden-Wuerttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thueringen'
        ) AND population <= '200000'
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


@app.get("/citiesmorethan200000")
async def get_data2():
    # do this for every visualisation that requires parts of the data
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = '''
            SELECT *
            FROM measles_data
            WHERE location NOT IN (
            'Baden-Wuerttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thueringen'
        ) AND population > '200000' 
              AND population < '500000';
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


@app.get("/citiesmorethan500000")
async def get_data2():
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = '''
            SELECT *
            FROM measles_data
            WHERE location NOT IN (
            'Baden-Wuerttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thueringen'
        ) AND population > '500000' 
              AND population < '1000000';
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


@app.get("/citiesmorethan1000000")
async def get_data2():
    conn = sqlite3.connect('data_for_web_application.db')
    cursor = conn.cursor()

    query = '''
            SELECT *
            FROM measles_data
            WHERE location NOT IN (
            'Baden-Wuerttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thueringen'
        ) AND population > '1000000';
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

@app.post("/uploadjson/")
async def upload_json(file: UploadFile = File(...)):
    # Check if the file extension is JSON
    if file.filename.endswith(".json"):
        try:
            # Read the JSON content from the uploaded file
            json_content = await file.read()
            decoded_json = json_content.decode("utf-8")

            # Save JSON data to a file named new_measles_data.json
            json_file_name = "new_measles_data.json"
            with open(json_file_name, "w") as json_file:
                json_file.write(decoded_json)
            # You can perform additional validation or processing here if needed
            json_in_db = JsonInDatabaseTranformer()
            json_in_db.push_json_data_in_db(json_file_name)
            return {"status": "File is correct", "json_content": json_content.decode("utf-8")}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing JSON file: {str(e)}")
    else:
        raise HTTPException(status_code=400, detail="Uploaded file must be a JSON file")


app.mount("/", StaticFiles(directory="./", html=True), name="/")
