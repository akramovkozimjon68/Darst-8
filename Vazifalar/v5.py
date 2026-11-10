import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}


matn = json.dumps(talaba, ensure_ascii=False)

print("JSON matn:")
print(matn)

yangi_talaba = json.loads(matn)

print("Talaba ismi:", yangi_talaba["ism"])