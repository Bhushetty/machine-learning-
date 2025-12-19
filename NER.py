import re

text = "Geethika is studying at Malla Reddy University in Hyderabad since 2023."


persons = ["Geethika", "Sai"]
locations = ["Hyderabad", "India", "Telangana"]
organizations = ["Malla Reddy University", "Google", "Microsoft"]

entities = []


for name in persons:
    if name in text:
        entities.append((name, "PERSON"))


for place in locations:
    if place in text:
        entities.append((place, "LOCATION"))

for org in organizations:
    if org in text:
        entities.append((org, "ORGANIZATION"))


dates = re.findall(r"\b\d{4}\b", text)
for date in dates:
    entities.append((date, "DATE"))


for entity in entities:
    print(entity)
