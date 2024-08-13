#sayı tahmin oyunu

import random
sayi = random.randint(1,10)
count = 0

for x in range(5):
    tahmin = int(input("Tahminin ne :"))
    count+=1
    if(tahmin > sayi):
        print("Aşağı")
    elif (tahmin < sayi):
        print("yukarı ")
    elif(tahmin == sayi):
        print(f"Tebrikler. sayıyı {count}.defada buldun.toplam puanınız {100-(20)*(count-1)}")
        break
print(f"Aklımdaki sayı {sayi} sayısıydı")


