sayi1 = int(input("1. sayıyı giriniz :"))
sayi2 = int(input("2. sayıyı giriniz :"))

# ebob bulma
ebob = 1
i = 1

while i <= sayi1 and i <= sayi2:
    if sayi1%i == 0 and sayi2%i == 0:
        ebob = i
    i += 1

# EKOK bulma

buyuk_sayi = max(sayi1,sayi2)

while True:
    if buyuk_sayi %sayi1 == 0 and buyuk_sayi%sayi2 == 0:
        ekok = buyuk_sayi
        break
    buyuk_sayi += 1 

# sonuç kısmı

print(sayi1," ve ",sayi2,"'nin ebobu :",ebob)
print(sayi1," ve ",sayi2,"'nin ekoku :",ekok)
