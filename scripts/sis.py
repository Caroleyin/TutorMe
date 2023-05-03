import requests
import json

url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=1232"

response = requests.get(url)

depts = []
for (key, value) in response.json().items():
    if key == 'subjects':
        for c in value:
            depts.append(c['subject'])

for i in depts:
    print(i)