import turtle
t=turtle.Turtle()
scr=t.getscreen()
#hiermee krijg je het object van de turtle terug

scr.bgcolor("Light Blue")
#hiermee kun je de achtergrond kleur veranderen 

t.pencolor("tan1")
#dit verandert de kleur van de pen

t.color("tan1")
#dit verandert de kleur waarmee je tekent

t.pensize(3)
#dit verandert de grootte van de pen

t.penup()
#hiermee zorg je ervoor dat je niks tekent

t.setheading(90)
#hiermee verander je waar de pen naar wijst

t.goto(30,-30)
#hiermee verplaats je de pen naar een andere plek
t.pendown()
#hiermee zorg je ervoor dat de pen gaat tekenen

t.begin_fill()
#hiermee ga je je tekening vulling geven

t.circle(45,180)
#hiermee teken je een cirkel

t.right(90)
#hiermee zet je de pen naar rechts

t.goto(-45,-30)
t.circle(35,190)
t.setheading(0)
t.forward(55)
#hiermee zet je de pen naar voren

t.penup()
t.setheading(0)
t.pendown()
t.circle(35,190)
t.penup()
t.end_fill()
#hiermee laat je je tekening gevuld worden

t.pencolor("DeepPink1")
t.color("Pink")
t.setheading(270)
t.goto(-10,-90)
t.right(60)
t.pendown()
t.begin_fill()
t.forward(15)
t.left(60)
#hiermee zet je de pen naar links

t.forward(10)
t.circle(10,180)
t.forward(10)
t.left(60)
t.forward(15)
t.end_fill()
t.pensize(1)
t.pencolor("DeepPink")
t.goto(-13,-90)
t.setheading(270)
t.forward(17)
t.circle(4,180)
t.penup()
t.left(90)
t.forward(8)
t.goto(-13,107)
t.goto(-13,-107)
t.setheading(270)
t.left(180)
t.pendown()
t.circle(4,-180)
t.end_fill()
t.penup()
t.goto(42,-45)
t.pencolor("black")
t.color("sienna")
t.setheading(0)
t.pendown()
t.begin_fill()
t.forward(10)
t.left(60)
t.circle(35,145)
t.end_fill()
t.penup()
t.goto(-70,-45)
t.pendown()
t.setheading(180)
t.begin_fill()
t.forward(10)
t.left(-240)
t.circle(35,-145)
t.end_fill()
t.penup()
t.pencolor("black")
t.color("black")
t.goto(-5,-45)
t.setheading(270)
t.pendown()
t.begin_fill()
t.circle(10,180)
t.forward(5)
t.circle(10,180)
t.forward(5)
t.end_fill()
t.penup()
t.pencolor("black")
t.color("black")
t.goto(-45,-45)
t.setheading(270)
t.pendown()
t.begin_fill()
t.circle(10,180)
t.circle(5)
t
t.circle(10,180)
t.forward(5)
t.end_fill()
t.penup()
t.color("white")
t.goto(-2,-44)
t.begin_fill()
t.circle(6)
t.end_fill()
t.color("white")
t.goto(-40,-44)
t.begin_fill()
t.circle(6)
t.end_fill()
t.color("black")
t.goto(-25,-75)
t.begin_fill()
t.circle(10)
t.end_fill()
t.goto(-14,-73)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.goto(-20,-73)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.goto(-17,-77)
t.color("white")
t.begin_fill()
t.circle(2)
t
t.end_fill()
t.hideturtle()
#hiermee verberg je de pen

