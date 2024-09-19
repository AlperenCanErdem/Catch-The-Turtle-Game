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

while 1==1:
    my_turtle_instance.hideturtle()
    a = random.choice(range(-350, 350))
    b = random.choice(range(-300, 300))
    my_turtle_instance.goto(x=a , y=b)
    my_turtle_instance.showturtle()
    time.sleep(2)


turtle.mainloop()