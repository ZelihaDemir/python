# Kütüphane içe aktarımı
import turtle

# pencere ayarları
wndw = turtle.Screen()
wndw.title("Python Türk Bayrağı")
wndw.setup(720,420)
wndw.bgcolor("red")

# Turle ayarları
kalem = turtle.Turtle()

# ilk daire
kalem.color("white")
kalem.penup()
kalem.goto(-120,-100)
kalem.pendown()
kalem.begin_fill()
kalem.circle(120)
kalem.end_fill()

#2. daire
kalem.color("red")
kalem.penup()
kalem.goto(-90,-80)
kalem.pendown()
kalem.begin_fill()
kalem.circle(100)
kalem.end_fill()


#yıldız
kalem.color("white")
kalem.penup()
kalem.goto(50,30)
kalem.pendown()
kalem.begin_fill()
for i in range(5):
    kalem.forward(60)
    kalem.right(144)
    kalem.forward(60)  # Yıldızın içini doldurmak için içeri doğru bir adım at
    kalem.left(72) 
kalem.end_fill()
#çizim sonu
kalem.hideturtle()

turtle.done()