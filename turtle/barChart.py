import turtle
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Bar Chart")

xs = [48,117,200,240,160,260,220]

def bar_chart(t,height):
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)  
    t.left(90)
    t.forward(10)

data = turtle.Turtle()
data.color("red")
data.pensize(3)

for v in xs:
    bar_chart(data,xs)

wn.mainloop()