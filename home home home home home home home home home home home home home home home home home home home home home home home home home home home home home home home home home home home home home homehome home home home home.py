import turtle

t = turtle.Turtle()
b = turtle.Screen()
b.bgcolor("Blue")

t = turtle.Turtle()
t.shape("triangle")
t.color("DeepSkyBlue")
t.fillcolor("DeepSkyBlue")


"""
t.forward (100)
t.left(90)

t.pensize(6)
t.fillcolor("Blue")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.backward(200)
t.pendown()
t.circle(50)
"""


t.penup()
t.goto(-50,-70)
t.pendown()
t.goto(-50,70)
t.goto(50,-70)
t.goto(50,70)
