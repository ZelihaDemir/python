# """
# inheritance (Kalıtım) : miras alna

# animal --> dog(),cat()   yani animalın sahip olduğu tüm özellikler doga ve cate de aittir

# """

# class Person:
#     def __init__(self,fname,lname):
#         self.firstName = fname
#         self.laseName = lname
#         print("person created")

#     def WhoAmI(self):
#         print("I am a person")

#     def eat(self):
#         print("I am eating")

# class Student(Person):
#     def __init__(self,fname,lname,number):
#         Person.__init__(self,fname,lname)
#         self.studentNumber = number
#         print("student created")

#     # def WhoAmI(self):
#     #     print("I am a student")
#     def sayHello(self):
#         print("hello ı am a student")


# class Teacher(Person):
#     def __init__(self, fname, lname,branch):
#         super().__init__(fname,lname)
#         self.branch = branch

#     def WhoAmI(self):
#         print(f"I am a {self.branch} teacher")



# p1 = Person("Hüseyin","Sağlam")
# s1 = Student("zeliha","demir",30721043)
# t1 = Teacher("serkan","yılmaz","math")

# print(s1.firstName+" "+s1.laseName+" "+str(s1.studentNumber))

# s1.WhoAmI()
# s1.eat()
# s1.sayHello()
# t1.WhoAmI()



class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi oluşturuldu")
    
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("movie silindi")

m = Movie("film adı","yönetmen adı",120)


# print(m)
# print(len(m))

del m

print(m)

