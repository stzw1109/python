import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing a Circle with Turtle")
screen.bgcolor("white")

# Create a turtle object
circle_turtle = turtle.Turtle()
circle_turtle.shape("turtle")
circle_turtle.color("blue")

# Draw a circle
circle_turtle.circle(100)  # The argument is the radius of the circle

# Hide the turtle (optional)
circle_turtle.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
