import turtle
import random
import time
game_screen = turtle.Screen()
game_screen.bgcolor("light blue")
game_screen.title("Catch The Turtle")

my_turtle_instance = turtle.Turtle()
my_turtle_instance.shape("turtle")
my_turtle_instance.shapesize(2.8)
my_turtle_instance.color("green")
my_turtle_instance.penup()
game_time = 60
game_time_instance = turtle.Turtle()
game_time_instance.penup()
game_time_instance.hideturtle()
game_time_instance.left(90)
game_time_instance.forward(300)
game_time_instance.write(f" Time: {game_time}")
game_score = 0
game_score_instance = turtle.Turtle()
game_score_instance.penup()
game_score_instance.hideturtle()
game_score_instance.left(90)
game_score_instance.forward(290)
game_score_instance.write(f" Score: {game_score}")


while game_time > 0:
    my_turtle_instance.hideturtle()
    a = random.choice(range(-350, 350))
    b = random.choice(range(-300, 300))
    my_turtle_instance.goto(x=a , y=b)
    my_turtle_instance.showturtle()
    time.sleep(2)
    game_time = game_time - 2
    game_time_instance.clear()
    game_time_instance.write(f" Time: {game_time}")
    game_score_instance.clear()
    game_score_instance.write(f"Score: {game_score}")






turtle.mainloop()