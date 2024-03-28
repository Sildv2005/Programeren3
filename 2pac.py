import turtle

# Functie om een cirkel te tekenen
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Functie om een ovaal te tekenen
def draw_oval(color, width, height, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(45)
    for _ in range(2):
        turtle.circle(width, 90)
        turtle.circle(height, 90)
    turtle.end_fill()

# Instellingen voor het tekenen
turtle.speed(2)
turtle.hideturtle()

# Hoofd
draw_circle("lightblue", 60, 0, -50)

# Haar
turtle.width(15)
turtle.color("black")
turtle.penup()
turtle.goto(-30, 20)
turtle.pendown()
turtle.setheading(240)
turtle.circle(70, 120)

# Ogen
draw_circle("white", 10, -20, 10)
draw_circle("white", 10, 20, 10)
draw_circle("black", 5, -20, 10)
draw_circle("black", 5, 20, 10)

# Wenkbrauwen
turtle.width(5)
turtle.penup()
turtle.goto(-30, 30)
turtle.pendown()
turtle.goto(-10, 40)
turtle.penup()
turtle.goto(30, 30)
turtle.pendown()
turtle.goto(10, 40)

# Neus
draw_circle("black", 3, 0, 0)

# Mond
turtle.penup()
turtle.goto(-15, -10)
turtle.pendown()
turtle.color("black")
turtle.width(3)
turtle.setheading(-60)
turtle.circle(15, 120)

# Oorbellen
draw_circle("yellow", 5, -50, -60)
draw_circle("yellow", 5, 50, -60)

# Tekst
turtle.penup()
turtle.goto(0, -150)
turtle.write("Billie Eilish", align="center", font=("Arial", 12, "normal"))

# Afsluiten
turtle.done()
