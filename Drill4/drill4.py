import turtle

turtle.left(90)
for x in range(0,6):
    turtle.forward(500)
    turtle.penup()
    turtle.goto((x+1) * 100, 0)
    turtle.pendown()

turtle.penup()
turtle.goto(0,0)
turtle.right(90)
turtle.pendown()

for y in range(0,6):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0, (y+1) * 100)
    turtle.pendown()
    

turtle.exitonclick()
