import turtle
colors = ['black','red','orange','purple','blue','green','yellow']

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tess!")

someShape = turtle.Turtle()
someShape.color("hotpink")
someShape.pensize(3)

someShape2 = turtle.Turtle()
someShape2.shape('turtle')
someShape2.color("hotpink")
someShape2.pensize(3)
someShape2.speed(10)

# someShape2.penup()
# someShape2.left(90)
# someShape2.forward(300)
# someShape2.pendown()


for i in range(6):
    someShape.forward(50)
    someShape.left(60)

for colour in colors:
    someShape2.stamp()
    someShape2.color(colour)
    someShape2.forward(50)
    someShape2.left(60)
    
wn.mainloop()