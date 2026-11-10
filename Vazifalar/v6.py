import csv

with open("Vazifalar/v6.json", "r", encoding="utf-8") as fayl:
    data = csv.DictReader(fayl)

    for row in data:
        print("Ism:", row["ism"])

        if int(row["yosh"]) > 20:
            print("20 yoshdan katta:", row["ism"])