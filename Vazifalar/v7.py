import csv

eng_qimmat = 0
qimmat_nomi = ""

with open("Vazifalarv7.json", "r", encoding="utf-8") as fayl:
    data = csv.DictReader(fayl)

    for row in data:
        nom = row["nom"]
        narx = int(row["narx"])
        miqdor = int(row["miqdor"])

        umumiy = narx * miqdor

        print("Mahsulot:", nom)
        print("Umumiy qiymati:", umumiy)

        if narx > eng_qimmat:
            eng_qimmat = narx
            qimmat_nomi = nom

print("Eng qimmat mahsulot:", qimmat_nomi)
print("Narxi:", eng_qimmat)