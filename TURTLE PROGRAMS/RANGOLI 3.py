import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
t.hideturtle()
colors=["red", "yellow", "blue", "green"]
for i in range(700):
    t.pencolor(colors[i%4])
    t.circle(i)
    t.left(90)
    
