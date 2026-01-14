import json

data={
    "name":"Ravi",
    "Age":25,
    "Skills":["python","java"]
}

with open('data.json', "w") as file:
    json.dump(data,file,indent=4)