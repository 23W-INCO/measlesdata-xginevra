import json
from decimal import Decimal
from fhir.resources.bundle import Bundle
from fhir.resources.observation import Observation
from fhir.resources.quantity import Quantity

# my existing .json data
data = [
    {
        "Bundesland": "Baden-Württemberg",
        "Masernzahlen": 2619,
        "Impfrate": 77.80,
        "Gesamtbevoelkerung": "10.879.618",
        "Per100000": 24.07
    },
    {
        "Bundesland": "Bayern",
        "Masernzahlen": 7148,
        "Impfrate": 76,
        "Gesamtbevoelkerung": "12.843.514",
        "Per100000": 55.65
    },
    {
        "Bundesland": "Berlin",
        "Masernzahlen": 2644,
        "Impfrate": 70,
        "Gesamtbevoelkerung": "3.520.031",
        "Per100000": 75.11
    },
    {
        "Bundesland": "Brandenburg",
        "Masernzahlen": 338,
        "Impfrate": 80.80,
        "Gesamtbevoelkerung": "2.484.826",
        "Per100000": 13.6
    },
    {
        "Bundesland": "Bremen",
        "Masernzahlen": 99,
        "Impfrate": 77.70,
        "Gesamtbevoelkerung": "671.489",
        "Per100000": 14.74
    },
    {
        "Bundesland": "Hamburg",
        "Masernzahlen": 551,
        "Impfrate": 83.80,
        "Gesamtbevoelkerung": "1.787.408",
        "Per100000": 30.83
    },
    {
        "Bundesland": "Hessen",
        "Masernzahlen": 1186,
        "Impfrate": 83.40,
        "Gesamtbevoelkerung": "6.176.172",
        "Per100000": 19.20
    },
    {
        "Bundesland": "Mecklenburg-Vorpommern",
        "Masernzahlen": 50,
        "Impfrate": 76.40,
        "Gesamtbevoelkerung": "1.612.362",
        "Per100000": 3.1
    },
    {
        "Bundesland": "Niedersachsen",
        "Masernzahlen": 2553,
        "Impfrate": 81.60,
        "Gesamtbevoelkerung": "7.926.599",
        "Per100000": 32.2
    },
    {
        "Bundesland": "Nordrhein-Westfalen",
        "Masernzahlen": 7368,
        "Impfrate": 83.30,
        "Gesamtbevoelkerung": "17.865.516",
        "Per100000": 41.24
    },
    {
        "Bundesland": "Rheinland-Pfalz",
        "Masernzahlen": 956,
        "Impfrate": 80.90,
        "Gesamtbevoelkerung": "4.052.803",
        "Per100000": 23.59
    },
    {
        "Bundesland": "Saarland",
        "Masernzahlen": 78,
        "Impfrate": 76.80,
        "Gesamtbevoelkerung": "995.597",
        "Per100000": 7.83
    },
    {
        "Bundesland": "Sachsen",
        "Masernzahlen": 565,
        "Impfrate": 27.50,
        "Gesamtbevoelkerung": "4.084.851",
        "Per100000": 13.83
    },
    {
        "Bundesland": "Sachsen-Anhalt",
        "Masernzahlen": 236,
        "Impfrate": 78.90,
        "Gesamtbevoelkerung": "2.245.470",
        "Per100000": 10.51
    },
    {
        "Bundesland": "Schleswig-Holstein",
        "Masernzahlen": 688,
        "Impfrate": 83.40,
        "Gesamtbevoelkerung": "2.858.714",
        "Per100000": 24.07
    },
    {
        "Bundesland": "Thüringen",
        "Masernzahlen": 357,
        "Impfrate": 71.90,
        "Gesamtbevoelkerung": "2.170.714",
        "Per100000": 16.44
    }
]


# Custom JSON encoder to handle Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


# Create FHIR-compatible JSON structure
fhir_data = {
    "resourceType": "Bundle",
    "type": "collection",
    "entry": []
}

for entry in data:
    observation = Observation(
        status="final",
        category=[
            {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "survey"}]}],
        code={"coding": [{"system": "http://loinc.org", "code": "8629-0"}], "text": "Measles Statistics"},
        subject={"reference": f"Location/{entry['Bundesland'].lower().replace(' ', '-')}"},
        component=[
            {"code": {"coding": [{"system": "http://loinc.org", "code": "8629-0"}], "text": "Measles Cases"},
             "valueQuantity": Quantity(value=entry["Masernzahlen"], unit="cases", system="http://unitsofmeasure.org",
                                       code="{cases}")
             },
            {"code": {"coding": [{"system": "http://loinc.org", "code": "VaccinationRate"}],
                      "text": "Vaccination Rate"},
             "valueQuantity": Quantity(value=entry["Impfrate"], unit="%", system="http://unitsofmeasure.org",
                                       code="{percent}")
             },
            {"code": {"coding": [{"system": "http://loinc.org", "code": "Per100000"}], "text": "Per 100,000"},
             "valueQuantity": Quantity(value=entry["Per100000"], unit="1/100000", system="http://unitsofmeasure.org",
                                       code="{1/100000}")
             },
            {"code": {"coding": [{"system": "http://loinc.org", "code": "Population"}], "text": "Population"},
             "valueQuantity": Quantity(value=float(entry["Gesamtbevoelkerung"].replace(".", "")), unit="individuals",
                                       system="http://unitsofmeasure.org", code="{individuals}")
             }
        ]
    )

    fhir_data["entry"].append({"resource": observation.dict()})

# Convert the FHIR-compatible data to JSON
fhir_json = json.dumps(fhir_data, indent=2, cls=DecimalEncoder)

# Save the JSON to a file
with open("measlesdata_fhir.json", "w") as f:
    f.write(fhir_json)

print("FHIR-compatible JSON file generated.")
