import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Joseph Gonzalez")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# First Paddle

first_paddle = turtle.Turtle()
first_paddle.speed(0)
first_paddle.shape("square")
first_paddle.color("white")
first_paddle.shapesize(stretch_wid=5, stretch_len=1)
first_paddle.penup()
first_paddle.goto(-350, 0)


# Second Paddle

second_paddle = turtle.Turtle()
second_paddle.speed(0)
second_paddle.shape("square")
second_paddle.color("white")
second_paddle.shapesize(stretch_wid=5, stretch_len=1)
second_paddle.penup()
second_paddle.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2


# Scoreboard

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 12, "normal"))

# Scoring
score_a = 0
score_b = 0

# Function

def first_paddle_up():
	y = first_paddle.ycor()
	y += 20
	first_paddle.sety(y)

def first_paddle_down():
	y = first_paddle.ycor()
	y -= 20
	first_paddle.sety(y)

def second_paddle_up():
	y = second_paddle.ycor()
	y += 20
	second_paddle.sety(y)

def second_paddle_down():
	y = second_paddle.ycor()
	y -= 20
	second_paddle.sety(y)

# Keyboard binding

wn.listen()
wn.onkeypress(first_paddle_up, "w")
wn.onkeypress(first_paddle_down, "s")
wn.onkeypress(second_paddle_up, "Up")
wn.onkeypress(second_paddle_down, "Down")


# Main Game

while True:
	wn.update()

	# Moving ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)


	# Adding Border
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
		
	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal"))

	# Paddle and Ball Touch
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < second_paddle.ycor() + 50 and ball.ycor() > second_paddle.ycor() -50):
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < first_paddle.ycor() + 50 and ball.ycor() > first_paddle.ycor() -50):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)