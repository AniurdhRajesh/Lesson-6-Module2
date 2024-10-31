import turtle
turtle.Screen().bgcolor("tan")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
no_sides=10
side_long=70
angle=36
for i in range(no_sides):
    turtle.forward(side_long)
    turtle.right(angle)