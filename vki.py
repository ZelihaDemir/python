print("Vucüt kitle indeksi hesaplama programına hoşgeldiniz")

agırlık = float(input("Ağırlığınızı giriniz (kg) :"))
boy = float(input("Boyunuzu giriniz (m):"))

vki = agırlık / (boy*boy)

if vki < 18.5:
    durum = "zayıf"
elif vki >18.5 and vki <24.9:
    durum = "Sağlıklı" 
elif vki>25 and vki <<29.9:
    durum = "Fazla kilolu"
else:
    durum = "Obezite"
print(vki,durum)