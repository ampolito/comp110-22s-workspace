"""Ex-04: An out-of-this world scene from space."""


__author__ = "730403071"


from turtle import Turtle, done


def draw_background(space: Turtle, x: float, y: float) -> None: 
    """The darkness of space."""
    space.penup()
    space.speed('fastest')
    space.goto(x, y)
    space.setheading(0)
    space.pendown()
    i: int = 0
    space.fillcolor("black")
    space.begin_fill()
    while i < 4:
        space.forward(9500)
        space.left(90)
        i += 1
    space.end_fill() 
        

def draw_rocket_body(louis: Turtle, x: float, y: float, width: float, length: float) -> None: 
    """This is my complex function that got broken up. Instead of writing one, long function for my rocket, I broke it up into the different rocket's components."""
    """These components can be found on lines 27-43, 46-57, 60-76, 79-94, and 97-110."""
    louis.penup()
    louis.goto(x, y)
    louis.pendown()
    louis.speed(10) 
    louis.fillcolor("white")
    louis.begin_fill()
    i: int = 0
    while i < 2: 
        louis.forward(width)
        louis.right(90)
        louis.forward(length)
        louis.right(90)
        i = i + 1
    louis.end_fill()


def draw_rocket_capsule(louis: Turtle, width: float) -> None: 
    """The creation of my rocket in space. This includes the top capsule of the rocket."""
    louis.penup()
    louis.pendown()
    louis.fillcolor("white")
    louis.begin_fill()
    i: int = 0
    while i < 3: 
        louis.forward(width)
        louis.left(120)
        i = i + 1
    louis.end_fill()


def draw_rocket_right_tail(louis: Turtle) -> None: 
    """The creation of my rocket's right tail in space."""
    louis.penup()
    louis.pendown()
    louis.fillcolor("white")
    louis.begin_fill() 
    louis.forward(100)
    louis.right(90)
    louis.forward(130)
    louis.left(35)

    louis.forward(100)
    louis.right(125)
    louis.forward(57)
    louis.right(90)
    louis.forward(12)
    louis.end_fill()


def draw_rocket_left_tail(louis: Turtle) -> None: 
    """The creation of my rocket's left tail."""
    louis.penup()
    louis.pendown()
    louis.begin_fill() 
    louis.color("white")
    louis.left(90)
    louis.forward(100)
    louis.left(90)

    louis.forward(12)
    louis.right(90)
    louis.forward(57)
    louis.right(125)
    louis.forward(100)
    louis.end_fill()


def draw_rocket_window(louis: Turtle) -> None: 
    """The creation of the rocket's window."""
    louis.penup()
    louis.right(55)
    louis.forward(25)
    louis.pendown()
    louis.begin_fill() 
    louis.color("black")
    louis.forward(50)
    louis.left(90)
    louis.forward(50)
    louis.left(90)
    louis.forward(50)
    louis.end_fill()
    

def draw_star(louis: Turtle, x: float, y: float) -> None:
    """Creation of different stars throughout space."""
    louis.penup()
    louis.goto(x, y)
    louis.setheading(40)
    louis.pendown()
    louis.speed(10) 
    louis.fillcolor("yellow")
    louis.begin_fill()
    i: int = 0
    while i < 5: 
        louis.forward(100)
        louis.right(144)
        i = i + 1
    louis.end_fill()
    

def draw_planet(planet: Turtle, x: float, y: float) -> None: 
    """Here I tried something fun -- I chose the circle function from the source provided in the instructions in order to create a planet."""
    planet.penup()
    planet.goto(x, y)
    planet.fillcolor("red")
    planet.begin_fill()
    planet.circle(50)
    planet.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    space: Turtle = Turtle()
    draw_background(space, -3000, -3000) 
    star: Turtle = Turtle()
    draw_star(star, 200, 240)
    draw_star(star, -200, 250)
    draw_star(star, 200, -200)
    draw_star(star, -300, 90)
    rocket: Turtle = Turtle()
    draw_rocket_body(rocket, -200, 0, 100, 200)
    draw_rocket_capsule(rocket, 100)
    draw_rocket_right_tail(rocket)
    draw_rocket_left_tail(rocket)
    draw_rocket_window(rocket)
    planet: Turtle = Turtle()
    draw_planet(planet, 145, 120)
    done()


if __name__ == "__main__":
    main()