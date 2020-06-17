import turtle
import random
import time


def goup():
    if headOfSnake.direction != "down":
        headOfSnake.direction = "up"

def godown():
    if headOfSnake.direction != "up":
        headOfSnake.direction = "down"

def goRight():
    if headOfSnake.direction != "left":
        headOfSnake.direction = "right"

def goleft():
    if headOfSnake.direction != "right":
        headOfSnake.direction = "left"

def move():
    if headOfSnake.direction == "up":
        y = headOfSnake.ycor()
        headOfSnake.sety(y + 20)
        #print(headOfSnake.ycor())

    if headOfSnake.direction == "down":
        y = headOfSnake.ycor()
        headOfSnake.sety( y - 20)
    if headOfSnake.direction == "right":
        x = headOfSnake.xcor()
        headOfSnake.setx(x + 20)
        #print(headOfSnake.xcor())

    if headOfSnake.direction == "left":
        x =headOfSnake.xcor()
        headOfSnake.setx(x -20)

def exitprogram():
    window.bye()

def start():
    headOfSnake.direction ="right"




window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width = 800,height = 600)
window.tracer(0)



screenWidth = (window.window_width()/2) - 3
screenHeight = (window.window_height()/2) - 3
Score = int(0)

#head of snake
headOfSnake = turtle.Turtle()
headOfSnake.speed(0)
headOfSnake.shape("square")
headOfSnake.color("white")
headOfSnake.fillcolor("white")
headOfSnake.shapesize(0.5,0.5)
headOfSnake.penup()
headOfSnake.goto(0,0)
headOfSnake.direction = "right"

segments=[]

#food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
color=['gray', 'black']
food.shapesize(0.5, 0.5)
food.penup()
food.goto(random.randint(-window.window_width()/2, window.window_width()/2), random.randint(-window.window_height()/2, window.window_height()/2))


#canv
canv = turtle.Turtle()
canv.speed(0)
canv.shapesize(stretch_wid=30 ,stretch_len=40)
canv.shape("square")
canv.color("white")
canv.fillcolor("")
canv.penup()
canv.goto(0, 0)

# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(screenWidth - 50, screenHeight - 30)
score.write("Score : {}".format(Score), move=False, align="center", font=("Arial", 12, "normal"))
score.hideturtle()


window.listen()
window.onkeypress(goup ,"Up")
window.onkeypress(godown ,"Down")
window.onkeypress(goleft ,"Left")
window.onkeypress(goRight ,"Right")
window.onkeypress(exitprogram,"Escape")




while True:
    window.update()
    food.fillcolor(color[random.randint(0, 1)])
    food.color(color[random.randint(0, 1)])


    time.sleep(0.10)

    if int(headOfSnake.distance(food)) < 15:
        Score += 1
        score.clear()
        score.write("Score : {}".format(Score), move=False, align="center", font=("Arial", 12, "normal"))
        food.goto(random.randint(-screenWidth + 5,screenWidth - 5) ,random.randint(-screenHeight + 5, screenHeight -5))
        print("getting it ")
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = headOfSnake.xcor()
        y = headOfSnake.ycor()
        segments[0].goto(x, y)
    move()

    if headOfSnake.xcor() >= screenWidth and headOfSnake.direction == "right":
        headOfSnake.setx(-screenWidth)

    if headOfSnake.xcor() <= -screenWidth and headOfSnake.direction == "left" :
        headOfSnake.setx(screenWidth)

    if headOfSnake.ycor() >= screenHeight and headOfSnake.direction == "up":
        headOfSnake.sety(-screenHeight)

    if headOfSnake.ycor() <= -screenHeight and headOfSnake.direction == "down":
        headOfSnake.sety(screenHeight)

    for segment in segments:
        if segment.distance(headOfSnake) < 10:
            time.sleep(2)
            # GameOver
            gameOver = turtle.Turtle()
            gameOver.speed(0)
            gameOver.color("white")
            gameOver.penup()
            gameOver.goto(0, 0)
            gameOver.write("Game Over", move=False, align="center", font=("Arial", 28, "normal"))
            gameOver.hideturtle()
            headOfSnake.goto(0, 0)
            time.sleep(1)
            gameOver.clear()
            headOfSnake.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
                
            segments.clear()
