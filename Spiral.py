import turtle
turtle.speed(10)
spiral=turtle.Screen()
spiral.bgcolor("tan")
spiral.title("Spiral")
mypen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        mypen.stamp()
        mypen.fd(size+1)
        mypen.left(90)
        size=size-5
    size=size+1