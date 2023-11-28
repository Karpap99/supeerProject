from turtle import*

color("black")
width(10000)
forward(1)


speed(0)
colorT = ["red", "blue", "purple", "yellow", "green", "orange", "red", "blue", "purple", "yellow", "green", "orange", "red", "blue", "purple", "yellow", "green", "orange", "red", "blue", "purple", "yellow", "green", "orange", "red", "blue", "purple", "yellow", "green", "orange", "red", "blue", "purple", "yellow", "green", "orange"]

width(1)
for i in range(36):
    color(colorT[i])
    for j in range(4):
        forward(100)
        left(90)
    left(10)
exitonclick()
