"""
taş-kağıt-makas oyunu

"""
import random

options = ["taş","kağıt","makas"]
choice = input("Taş mı kağıt mı yoksa makas mı?\n")

pc = random.choice(options)
print("Bilgisayarın seçimi :",pc)

if choice == pc:
    print("Berabere!")
elif (choice =="taş" and pc =="makas") or (choice=="kağıt" and pc =="taş") or (choice=="makas" and choice=="kağıt"):
    print("Tebrikler ,kazandınız")
else:
    print("Bilgisayar kazandı")



