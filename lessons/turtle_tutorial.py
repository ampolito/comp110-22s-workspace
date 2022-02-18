from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()


# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)

# i: int = 0 
# while (i < 4):
#  leo.forward(300)
#  leo.left(120)
#  i = i + 1 

leo.begin_fill() 
leo.color("red")
colormode(255)
leo.color(99, 204, 250)
leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.goto(45, 60)
# to set only pen color: <turtlevariable>.pencolor(<color>)
# To move the turtle to a new x, y position: <turtlevariable>.goto(<x_coordinate>,<y_coordinate>):

# To prevent the turtle from drawing: <turtlevariable>.penup() or <turtlevariable>.up()
# To allow the turtle to draw: <turtlevariable>.pendown() or <turtlevariable>.down()

i: int = 0 
while (i < 3): 
    leo.forward(300)
    leo.left(120)
    i = i + 1 

# code for shape to be filled
leo.end_fill()

leo.speed(50)
leo.hideturtle()
done()

# leo.pencolor("pink")
# leo.fillcolor(32, 67, 93)
# leo.color("green", "yellow")

bob: Turtle = Turtle() 
bob.color("black")
colormode(255)
bob.color(11, 11, 11)
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.goto(45, 60)

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120) 
    i = i + 1 
