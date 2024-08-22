import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

nibba = turtle.Turtle()
nibba.color("orange")
nibba.pensize(3)

hexagon = turtle.Turtle()
hexagon.color("blue")
hexagon.pensize(3)

tess.left(135)
tess.forward(150)
tess.right(60)
tess.forward(40)
tess.right(30)
tess.forward(40)
tess.right(50)
tess.forward(40)
tess.right(30)
tess.forward(40)

nibba.right(315)
nibba.forward(150)
nibba.left(60)
nibba.forward(40)
nibba.left(30)
nibba.forward(40)
nibba.left(50)
nibba.forward(40)
nibba.left(30)
nibba.forward(40)



wn.mainloop()