import json

with open("Vazifalar/v3.json", "r") as fayl:
    data = json.load(fayl)

data["ball"] = 95

with open("Vazifalar/v3.json", "w") as fayl:
    json.dump(data, fayl, indent=4, ensure_ascii=False)

print("Ma'lumot yangilandi!")
print(data)