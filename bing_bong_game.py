#imported turtule module
from tkinter import W
import turtle

wind = turtle.Screen() # intialize screen
wind.title("ping pong prod py hisoka") #pick a title
wind.bgcolor("black") #pick a color
wind.setup(width=800, height=600) #the width and height of screen
wind.tracer(0) #stop the window updated automatically
 
#peddle1
peddle1 = turtle.Turtle() #intialazed turtle object
peddle1.speed(0) #the speed of animation
peddle1.shape("square") #set the shape of object
peddle1.shapesize(stretch_wid=5, stretch_len=1) #streches the shape to meet the size
peddle1.color("red") #the color of the shape
peddle1.penup() #stop the object from drowing size
peddle1.goto(-350, 0) #set the position

#peddle2peddle1 = turtle.Turtle()
peddle2 = turtle.Turtle()
peddle2.speed(0)
peddle2.shape("square")
peddle2.shapesize(stretch_wid=5, stretch_len=1)
peddle2.color("blue")
peddle2.penup()
peddle2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()   
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2


#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player1: 0 player2: 0", align="center" , font=("courier",24,"normal"))


#the functions
def peddle1_up():
    y = peddle1.ycor() #get the y coordinate of the peddle1
    y += 20 #set the y incraese be 20
    peddle1.sety(y) #set the y of the peddle to to the new y coordinate

def peddle1_down():
    y = peddle1.ycor()
    y -= 20
    peddle1.sety(y)

def peddle2_up():
    y = peddle2.ycor()
    y += 20
    peddle2.sety(y)

def peddle2_down():
    y = peddle2.ycor()
    y -= 20
    peddle2.sety(y)
    
#keyboard binding
wind.listen()#tell the window to expect input
wind.onkeypress(peddle1_up, "w")
wind.onkeypress(peddle1_down, "s")
wind.onkeypress(peddle2_up, "Up")
wind.onkeypress(peddle2_down, "Down")

#bild game loop
while True :
    wind.update()#updates the screen every time the game(lops) run 

    #move the ball
    ball.setx(ball.xcor() + ball.dx)#ball star at 0 and evry time loop run--->+0.5 xaxis
    ball.sety(ball.ycor() + ball.dy)#ball star at 0 and evry time loop run--->+0.5 yaxis

    #border check , top border +300px , battom border -300px , ball is 20px
    if ball.ycor() >290:#if ball at the top border 
       ball.sety(290)#set y coordinate +290
       ball.dy *= -1#reverse diraction ,making +0.5--->-0.5

    if ball.ycor() <-290:#if ball at bottom border
       ball.sety(-290)#set y coordinate -290
       ball.dy *= -1#reverse diraction ,making +0.5--->-0.5

    if ball.xcor() > 390:#if ball at the right border
        ball.goto(0, 0)#retern ball to the center
        ball.dx *= -1#reverse the x diraction
        score1 += 1
        score.clear() 
        score.write("player1: {} player2: {}".format(score1, score2), align="center" , font=("courier",24,"normal"))

    if ball.xcor() < -390:#if ball at the left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write("player1: {} player2: {}".format(score1, score2), align="center" , font=("courier",24,"normal"))

    
    #peddle and ball collision
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < peddle2.ycor() + 40 and ball.ycor() > peddle2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < peddle1.ycor() + 40 and ball.ycor() > peddle1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


    
    
    
