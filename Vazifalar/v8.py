import csv

ism = input("Ismni kiriting: ")
yosh = input("Yoshni kiriting: ")
kurs = input("Kursni kiriting: ")

with open("Vazifalar/v8.json", "a", encoding="utf-8", newline="") as fayl:
    writer = csv.writer(fayl)
    writer.writerow([ism, yosh, kurs])

print("Yangi o'quvchi qo'shildi!")

with open("Vazifalar/v8.json", "r", encoding="utf-8") as fayl:
    data = csv.reader(fayl)

    for row in data:
        print(row)