import turtle
t = turtle.Turtle()
turtle.tracer(4)
t.pensize(5)
t.hideturtle()
t.color('red')

t.setheading(0)
t.begin_fill()
t.circle(70)
t.end_fill()

t.setheading(72)
t.begin_fill()
t.circle(70)
t.end_fill()

t.setheading(144)
t.begin_fill()
t.circle(70)
t.end_fill()

t.setheading(216)
t.begin_fill()
t.circle(70)
t.end_fill()

t.setheading(288)
t.begin_fill()
t.circle(70)
t.end_fill()

t.color('yellow')
t.goto(-70,0)
t.setheading(-90)
t.begin_fill()
t.circle(70)
t.end_fill()