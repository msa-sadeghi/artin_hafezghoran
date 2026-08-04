# name = input("enter the name: ")
# with open("test", "w") as file:
#     file.write(name + "\n")


# with open("test", "r") as my_file:
#     name = my_file.read()
#     print(name.strip())

import turtle




def my_goto(x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

def draw_shape(n, length, color, speed):
    my_turtle.pencolor(color)
    my_turtle.speed(speed)
    my_turtle.begin_fill()
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(360 / n)
    my_turtle.end_fill()

screen = turtle.Screen()

screen.register_shape("firststeps.gif")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(4, 2, 5)
my_turtle.color("darkgreen")
my_turtle.pencolor("#8a5005")j
my_turtle.pensize(3)
my_goto(-200, 0)

num_of_sides = int(screen.textinput("sides", "how many sides? "))
length = int(screen.textinput("length", "enter the length you want "))
color = screen.textinput("color", "which  color you want ")
speed = screen.textinput("speed", "what speed you want ")

draw_shape(num_of_sides, length, color, speed)

my_goto(0, -200)
draw_shape(5, 100, "purple", "fast")

my_goto(200, 0)
draw_shape(6, 100, "orange", "fastest")

turtle.done()
