import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightyellow")
t.speed(0)

# Pétalos
t.color("deeppink", "hotpink")
for _ in range(12):
    t.begin_fill()
    for _ in range(2):
        t.circle(80, 60)
        t.left(120)
    t.end_fill()
    t.left(30)

# Centro
t.penup()
t.goto(0, -15)
t.pendown()
t.color("orange", "gold")
t.begin_fill()
t.circle(15)
t.end_fill()

# Tallo
t.penup()
t.goto(0, -15)
t.setheading(-90)
t.pensize(6)
t.color("forestgreen")
t.pendown()
t.forward(200)

# Hoja
t.penup()
t.goto(0, -120)
t.setheading(-30)
t.pendown()
t.begin_fill()
for _ in range(2):
    t.circle(50, 60)
    t.left(120)
t.end_fill()

t.hideturtle()
screen.mainloop()