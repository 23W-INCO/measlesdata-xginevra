import json
from decimal import Decimal

from fhir.resources.observation import Observation
from fhir.resources.quantity import Quantity


# this is the python file I used to make the .json file FHIR compatible
# I created the .json file with jsongen.py.

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


# Sample data
with open("merged_data_fhir.json") as json_data:  # replace the name if needed, i did several Umwege hilariously
    data = json.load(json_data)

# Create FHIR-compatible JSON structure
fhir_data = {
    "resourceType": "Bundle",
    "type": "collection",
    "entry": []
}
measle_data = data["entry"]

for resource in measle_data:
    entry = resource["resource"]
    componets_list = [
        {"code": {"coding": [{"system": "http://loinc.org", "code": "8629-0"}], "text": "Measles Cases"},
         "valueQuantity": Quantity(value=entry["cases"], unit="cases", system="http://unitsofmeasure.org",
                                   code="{cases}")
         },

        {"code": {"coding": [{"system": "http://loinc.org", "code": "totalPopulation"}], "text": "Population"},
         "valueQuantity": Quantity(value=float(entry["totalPopulation"].replace(".", "")), unit="individuals",
                                   system="http://unitsofmeasure.org", code="{individuals}")
         }
    ]
    if "vaccinationRate" in entry:
        new = {
            "code": {"coding": [{"system": "http://loinc.org", "code": "VaccinationRate"}], "text": "Vaccination Rate"},
            "valueQuantity": Quantity(value=entry["vaccinationRate"], unit="%", system="http://unitsofmeasure.org",
                                      code="{percent}")
        }
        componets_list.append(new)
    if "casesPer100000" in entry:
        new = {"code": {"coding": [{"system": "http://loinc.org", "code": "Per100000"}], "text": "Per 100,000"},
               "valueQuantity": Quantity(value=entry["casesPer100000"], unit="1/100000",
                                         system="http://unitsofmeasure.org", code="{1/100000}")
               }
        componets_list.append(new)
    observation = Observation(
        status="final",
        category=[
            {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "survey"}]}],
        code={"coding": [{"system": "http://loinc.org", "code": "8629-0"}], "text": "Measles Statistics"},
        subject={"reference": f"Location/{entry['name'].lower().replace(' ', '-')}"},
        component=componets_list
    )

    fhir_data["entry"].append({"resource": observation.dict()})
# measle_data = data["entry"]
# for resource in measle_data:
#     entry = resource["resource"]
#     observation = {
#         "resourceType": "Observation",
#         "status": "final",
#         "category": [
#             {
#                 "coding": [
#                     {
#                         "system": "http://terminology.hl7.org/CodeSystem/observation-category",
#                         "code": "survey"
#                     }
#                 ]
#             }
#         ],
#         "code": {
#             "coding": [
#                 {
#                     "system": "http://loinc.org",
#                     "code": "8629-0"
#                 }
#             ],
#             "text": "Measles Statistics"
#         },
#         "subject": {
#             "reference": f"Location/{entry['name'].lower().replace(' ', '-')}"
#         },
#         "valueQuantity": {
#             "value": entry["cases"],
#             "unit": "cases",
#             "system": "http://unitsofmeasure.org",
#             "code": "{cases}"
#         },
#         # "VaccinationRate": {
#         #     "value": entry['vaccinationRate'],
#         #     "unit": "%",
#         #     "system": "http://unitsofmeasure.org",
#         #     "code": "{percent}"
#         # },
#         # "Per100000": {
#         #     "value": entry['casesPer100000'],
#         #     "unit": "1/100000",
#         #     "system": "http://unitsofmeasure.org",
#         #     "code": "{1/100000}"
#         # },
#         "Population": {
#             "value": float(entry['totalPopulation'].replace(".", "")),
#             "unit": "individuals",
#             "system": "http://unitsofmeasure.org",
#             "code": "{individuals}"
#         }
#     }
#     if "vaccinationRate" in entry:
#         observation["VaccinationRate"] = {
#             "value": entry['vaccinationRate'],
#             "unit": "%",
#             "system": "http://unitsofmeasure.org",
#             "code": "{percent}"
#         }
#     if "casesPer100000" in entry:
#         observation["Per100000"] = {
#             "value": entry['casesPer100000'],
#             "unit": "1/100000",
#             "system": "http://unitsofmeasure.org",
#             "code": "{1/100000}"
#         }
#     fhir_data["entry"].append({"resource": observation})

# Convert the FHIR-compatible data to JSON
fhir_json = json.dumps(fhir_data, indent=2, cls=DecimalEncoder)

# Save the JSON to a file
with open("measles_statistics_fhir.json", "w") as f:
    f.write(fhir_json)

print("FHIR-compatible JSON file generated.")
