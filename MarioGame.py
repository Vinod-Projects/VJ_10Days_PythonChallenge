
import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.title("Simple Mario Game")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Ground
ground = turtle.Turtle()
ground.penup()
ground.goto(-400, -180)
ground.color("green")
ground.pensize(10)
ground.pendown()
ground.goto(400, -180)
ground.hideturtle()

# Mario
mario = turtle.Turtle()
mario.shape("square")
mario.color("red")
mario.penup()
mario.goto(-250, -150)

# Coin
coin = turtle.Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.goto(200, -130)

# Obstacle
obstacle = turtle.Turtle()
obstacle.shape("square")
obstacle.color("brown")
obstacle.penup()
obstacle.goto(100, -150)

# Game variables
score = 0
y_speed = 0
on_ground = True
game_running = True

# Score display
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 250)
pen.write("Score: 0", align="center",
          font=("Arial", 20, "bold"))

# Movement functions
def move_left():
    if mario.xcor() > -380:
        mario.setx(mario.xcor() - 20)

def move_right():
    if mario.xcor() < 380:
        mario.setx(mario.xcor() + 20)

def jump():
    global y_speed, on_ground

    if on_ground:
        y_speed = 15
        on_ground = False

# Keyboard controls
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(jump, "space")

# Main game loop
while game_running:
    screen.update()

    # Gravity and jumping
    y_speed -= 0.7
    mario.sety(mario.ycor() + y_speed)

    # Ground collision
    if mario.ycor() <= -150:
        mario.sety(-150)
        y_speed = 0
        on_ground = True

    # Coin collection
    if mario.distance(coin) < 25:
        coin.goto(random.randint(-350, 350),
                  random.randint(-120, 150))

        score += 10
        pen.clear()
        pen.write("Score: " + str(score),
                  align="center",
                  font=("Arial", 20, "bold"))

    # Obstacle collision
    if mario.distance(obstacle) < 25:
        pen.goto(0, 0)
        pen.write("GAME OVER!",
                  align="center",
                  font=("Arial", 30, "bold"))
        screen.update()
        time.sleep(2)
        game_running = False

    time.sleep(0.02)

screen.mainloop()
