# # Nesne Tabanlı programlama

# # class

# class Person:
#     #  class attributes
#     address = "no information"

#     #constructor( yapıcı metod)
#     def __init__(self,name,year):
        
#         #  object attributes
#         self.name = name
#         self.year = year
    
#      #methods
#     def intro (self):
#         print("hello there.I am "+self.name)

#     def calculateAge(self):
#         return 2024 - self.year

# #object, instance
# p1 = Person(name = "zeliha",year = 2002)
# # print(p1)
# # print(type(p1))

# p2 = Person(name = "hüseyin",year = 2000)
# # print(p2)
# # print(type(p2))

# # print(p1 == p2)

# p1.intro()
# p2.intro()
# print(f"adım : {p1.name} ve yaşım : {p1.calculateAge()}")
# print(f"adım : {p2.name} ve yaşım : {p2.calculateAge()}")



class Circle:
    # ortak değerleri buraya yazıyoruz
    pi = 3.14

    def __init__(self,yarıcap = 1):
        # ortak olmayan değerleri ,kullanıcının farklı farklıgirmek istediği değerleri buraya
        self.yarıcap = yarıcap

    def cevreHesapla(self):
        return 2*self.pi*self.yarıcap
    
    def alanHesapla(self):
        return self.pi*(self.yarıcap**2)
    
c1 = Circle()
c2 = Circle(5)

print(f"c1 : alan {c1.alanHesapla()} çevre : {c1.cevreHesapla()}")
print(f"c2 : alan {c2.alanHesapla()} çevre : {c2.cevreHesapla()}")





