import time
from playsound import playsound


print(" sayaç programına hoşgeldiniz...")

dkvesn = input("Dakika ve saniyeyi giriniz.(örn.  '0 30' 30 saniye eder) : \n")
dk, sn = dkvesn.split()
dk = int(dk)
sn = int(sn)

sn = dk*60 + sn 

for sayac in range(sn,0,-1):
    print(sayac)
    time.sleep(1)

print("--------------süre doldu----------------")
playsound("Athena - Beyoğlu(_ywLtQ1zzGQo_).m4a")



