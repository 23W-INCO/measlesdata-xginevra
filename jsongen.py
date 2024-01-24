import pandas as pd
import json
import chardet
from fhir.resources.researchstudy import A


# This is the file I used to create a json out of the .csv file, though it was not FHIR compatible so far;
# to make it FHIR compatible - I used the create_fhir_json.py.

# Function to detect the encoding of a file
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


# Load CSV files with detected encoding
fallzahlen_df = pd.read_csv("fallzahlennachbundesland.csv", encoding=detect_encoding("fallzahlennachbundesland.csv"))
cities_cases_df = pd.read_csv("citiescases_neu.csv", encoding=detect_encoding("citiescases_neu.csv"))

# Create FHIR-like resources
fhir_resources = []

# Add MeaslesData resources
for _, entry in fallzahlen_df.iterrows():
    resource = {
        "resourceType": "MeaslesData",
        "location": entry["Bundesland"],
        "cases": entry["Masernzahlen"],
        "vaccinationRate": entry["Impfrate"],
        "totalPopulation": entry["Gesamtbevoelkerung"],
        "casesPer100000": entry["Per100000"]
    }
    fhir_resources.append(resource)

# Add CityCasesData resources
for _, entry in cities_cases_df.iterrows():
    resource = {
        "resourceType": "CityCasesData",
        "location": entry["Stadt"],
        "cases": entry["Cases"],
        "population": entry["Einwohnerzahl"]
    }
    fhir_resources.append(resource)

# Create a FHIR Bundle
fhir_bundle = {
    "resourceType": "Bundle",
    "type": "collection",
    "entry": [{"resource": res} for res in fhir_resources]
}

# Convert to JSON
json_data = json.dumps(fhir_bundle, indent=2)

# Write JSON data to a file
with open("merged_data_fhir.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print("FHIR-like JSON data has been saved to merged_data_fhir.json.")
