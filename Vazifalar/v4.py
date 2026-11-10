import json

with open("Vazifalar/v4.json", "r", encoding="utf-8") as fayl:
    data = json.load(fayl)

print("Telefon modeli:", data["model"])

yangi_narx = int(input("Yangi narxni kiriting: "))

data["narx"] = yangi_narx

with open("Vazifalar/v4.json", "w", encoding="utf-8") as fayl:
    json.dump(data, fayl, indent=4, ensure_ascii=False)

print("Telefon narxi yangilandi!")
print("Yangi narx:", data["narx"])