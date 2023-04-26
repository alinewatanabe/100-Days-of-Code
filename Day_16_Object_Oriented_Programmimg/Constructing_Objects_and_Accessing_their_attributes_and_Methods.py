from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("black", "Cadetblue")
# timmy.circle(50)
for i in range(0,4):
    timmy.forward(100)
    timmy.left(90)
timmy.forward(200)
timmy.left(90)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()