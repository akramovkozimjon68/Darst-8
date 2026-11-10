import csv

jami = 0
eng_katta = 0
eng_katta_nomi = ""
soni = 0

with open("Vazifalar/v9.json", "r", encoding="utf-8") as fayl:
    data = csv.DictReader(fayl)

    for row in data:
        nom = row["nom"]
        summa = int(row["summa"])

        jami += summa
        soni += 1

        if summa > eng_katta:
            eng_katta = summa
            eng_katta_nomi = nom

print("Jami xarajat:", jami)
print("Eng katta xarajat:", eng_katta_nomi)
print("Eng katta summa:", eng_katta)
print("Xarajatlar soni:", soni)