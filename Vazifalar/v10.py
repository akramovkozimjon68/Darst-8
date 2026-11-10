import csv

eng_yuqori = 0
eng_yuqori_ism = ""

with open("Vazifalar/v10.json", "r", encoding="utf-8") as fayl:
    data = csv.DictReader(fayl)

    for row in data:
        ism = row["ism"]
        sport = row["sport"]
        ball = int(row["ball"])

        print("Ism:", ism, "| Sport:", sport, "| Ball:", ball)

        if ball > 80:
            print("80 dan yuqori ball:", ism)

        if ball > eng_yuqori:
            eng_yuqori = ball
            eng_yuqori_ism = ism

print("\nEng yuqori ball olgan sportchi:", eng_yuqori_ism)
print("Ball:", eng_yuqori)