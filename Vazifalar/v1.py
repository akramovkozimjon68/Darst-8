import json

with open("Vazifalar/v1.json", "r", encoding="utf-8") as fayl:
    data = json.load(fayl)

print("Ism:", data["ism"])
print("Yosh:", data["yosh"])
print("Shahar:", data["shahar"])