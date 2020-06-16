import turtle

def player1_UP():
    y = player_1.ycor()
    if y < wind.canvheight - 70:
       #print(y, wind.canvheight)
        y += 10
        player_1.sety(y)

def player1_Down():
    y = player_1.ycor()
    #print(y, wind.canvheight)
    if y >= -(wind.canvheight - 80):
        y -= 10
        player_1.sety(y)

def player2_UP():
    y = player_2.ycor()
    if y < wind.canvheight - 70:
        #print(y, wind.canvheight)
        y += 10
        player_2.sety(y)

def player2_Down():
    y = player_2.ycor()
    #print(y, wind.canvheight)
    if y >= -(wind.canvheight - 80):
        y -= 10
        player_2.sety(y)

def exitprogram():
    wind.bye()

wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)
player1_score = 0
player2_score = 0





#Player_1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.shapesize(stretch_wid=6,stretch_len=1)
player_1.color("blue")
player_1.penup()
player_1.goto(-350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

#Player_2_
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.shapesize(stretch_wid=6,stretch_len=1)
player_2.color("red")
player_2.penup()
player_2.goto(350, 0)

#score
score =turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 :{}  Player 2 :{}".format(player1_score,player2_score), align="center", font=("Courier",28,"normal"))


# Canv
canv = turtle.Turtle()
canv.speed(0)
canv.shapesize(30,40)
canv.shape("square")
canv.color("white")
canv.fillcolor("")
canv.penup()
canv.goto(0, 0)

wind.listen() # Make window to expect input
wind.onkeypress(player1_UP,"w")
wind.onkeypress(player1_Down,"s")
wind.onkeypress(player2_UP,"Up")
wind.onkeypress(player2_Down,"Down")
wind.onkeypress(exitprogram,"Escape")

canvHeight = wind.canvheight - 10
canvWidth = wind.canvwidth - 20

while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > canvHeight :#if ball is at up border
        ball.sety(canvHeight)
        #print(wind.canvheight)
        ball.dy *= -1
    if ball.xcor() > canvWidth : #if ball is at right border
        player1_score +=1
        score.clear()
        score.write("Player 1 :{}  Player 2 :{}".format(player1_score, player2_score), align="center",
                    font=("Courier", 28, "normal"))
        ball.setx(0)
        #print(wind.canvwidth)
        ball.dx *= -1

    if ball.ycor() < -canvHeight :#if ball is at down border
        ball.sety(-canvHeight)
        ball.dy *= -1

        #print(ball.dy)
    if ball.xcor() < -canvWidth : #if ball is at left border
        ball.setx(0)
        player2_score +=1
        score.clear()
        score.write("Player 1 :{}  Player 2 :{}".format(player1_score, player2_score), align="center",
                    font=("Courier", 28, "normal"))
        ball.dx *= -1


    if ( ball.xcor() > player_2.xcor()-20 and ball.xcor() < player_2.xcor()) \
            and (ball.ycor() <  player_2.ycor()+60 and ball.ycor() > player_2.ycor()-60):
        ball.setx(player_2.xcor() - 20)
        ball.dx *=-1
        print("player 2")

    if ( ball.xcor() < player_1.xcor()+20 and ball.xcor() > player_1.xcor()) \
            and (ball.ycor() <  player_1.ycor()+60 and ball.ycor() > player_1.ycor()-60):
        ball.setx(player_1.xcor() + 20)
        ball.dx *=-1
        print("player 1")











