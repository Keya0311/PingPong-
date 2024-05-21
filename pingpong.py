#!/usr/bin/env python3
import turtle
window=turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)
#creating variable for the score
score_a=0
score_b=0

#Paddle Left
Paddle_L=turtle.Turtle()
Paddle_L.speed(0)
Paddle_L.shape("square")
Paddle_L.color("blue")
Paddle_L.penup()
Paddle_L.goto(-350,0)
Paddle_L.shapesize(stretch_wid=5,stretch_len=1)


#Paddle Right
Paddle_R=turtle.Turtle()
Paddle_R.speed(0)
Paddle_R.shape("square")
Paddle_R.color("red")
Paddle_R.penup()
Paddle_R.goto(350,0)
Paddle_R.shapesize(stretch_wid=5,stretch_len=1)

#The Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx=0.10
ball.dy=0.10

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0, Player B: 0",align ="center", font=("courier", 24, "normal"))


#moving the paddles


def Paddle_L_Up():
    y=Paddle_L.ycor()
    y=y+20
    Paddle_L.sety(y)

def Paddle_R_Down():
    y=Paddle_R.ycor()
    y=y-20
    Paddle_R.sety(y)

def Paddle_L_Down():
    y=Paddle_L.ycor()
    y=y-20
    Paddle_L.sety(y)

def Paddle_R_Up():
    y=Paddle_R.ycor()
    y=y+20
    Paddle_R.sety(y)    

#keyboard Binding
window.listen()
window.onkeypress(Paddle_L_Up ,"w")
window.onkeypress(Paddle_L_Down ,"s")
window.onkeypress(Paddle_R_Up ,"Up")
window.onkeypress(Paddle_R_Down ,"Down")
    

while True:
    window.update()
    newx=ball.xcor()+ball.dx
    newy=ball.ycor()+ball.dy
    ball.setx(newx)
    ball.sety(newy)

#border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy=ball.dy* -1
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy=ball.dy* -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
    elif ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1

    if (-350<ball.xcor()<-340) and ball.ycor()<Paddle_L.ycor()+50 and ball.ycor()>Paddle_L.ycor()-50:
        ball.dx=ball.dx*-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b),align ="center", font=("courier", 24, "normal"))
        
    
    if (340<ball.xcor()<350) and ball.ycor()<Paddle_R.ycor()+50 and ball.ycor()>Paddle_R.ycor()-50:
        ball.dx=ball.dx*-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b),align ="center", font=("courier", 24, "normal"))
    




