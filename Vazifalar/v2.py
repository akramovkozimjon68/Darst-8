import json

with open("Vazifalar/v2.json", "r", encoding="utf-8") as fayl:
    data = json.load(fayl)

umumiy = data["narx"] * data["miqdor"]

print("Mahsulot:", data["nom"])
print("Umumiy qiymat:", umumiy)