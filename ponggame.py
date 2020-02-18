#First have the graphical module in the base and turtle is the graphical module unit to build a graphical unit of a game!!!!
import turtle

window = turtle.Screen()
window.title("Pong game by Mangaldeep")
window.bgcolor("black")
window.setup(width=800, height= 600)
window.tracer(0)

#SCORE
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("yellow")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.shape("square")
paddle_b.goto(350,0)

#Ball

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("red")
ball.goto(0,0)
ball.speed(0)
ball.dx = 0.05
ball.dy = 0.05

#SCORE_desIGN
wr =  turtle.Turtle()
wr.speed(0)
wr.color("white")
wr.penup()
wr.hideturtle()
wr.goto(0,260)
wr.write("Player A: 0 Player B: 0", align="center", font =("Courier",24, "normal"))
#Function for paddle A for up and down
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=30
    paddle_a.sety(y)

#function for paddleB for up and down
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
        y = paddle_b.ycor()
        y -= 30
        paddle_b.sety(y)    


window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, 8)
window.onkeypress(paddle_b_down, 2)

# Main game loop
while True:
    window.update()
    #Movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a +=1
        wr.clear()
        wr.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font =("Courier",24, "normal"))
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b+=1
        wr.clear()
        wr.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font =("Courier",24, "normal"))
        ball.dx *= -1

    if paddle_a.ycor() > 290:
        paddle_a.sety(290-1)

    if paddle_a.ycor() < -290:
        paddle_a.sety(-291)   

    if paddle_b.ycor() < -290:
        paddle_b.sety(-291) 
        
    if paddle_b.ycor() > 290:
        paddle_b.sety(290-1)       
     

        #paddle and ball collision
    if (ball.xcor()> 340 and ball.xcor()<350) and(ball.ycor() < paddle_b.ycor() +40 and ball.ycor()> paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()< -340 and ball.xcor()> -350) and(ball.ycor() < paddle_a.ycor() +40 and ball.ycor()> paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1   

