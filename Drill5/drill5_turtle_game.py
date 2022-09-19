import turtle

def GoStraight():
    turtle.stamp()
    turtle.forward(50)

def MoveLeft():
    turtle.setheading(180)
    GoStraight()

def MoveRight():
    turtle.setheading(0)
    GoStraight()
    
def MoveUp():
    turtle.setheading(90)
    GoStraight()
    
def MoveDown():
    turtle.setheading(-90)
    GoStraight()

def Restart():
    turtle.reset()
    
    
turtle.shape('turtle')
turtle.onkey(MoveUp,'w')
turtle.onkey(MoveLeft,'a')
turtle.onkey(MoveDown,'s')
turtle.onkey(MoveRight,'d')
turtle.onkey(Restart,'Escape')
turtle.listen()

turtle.exitonclick()
