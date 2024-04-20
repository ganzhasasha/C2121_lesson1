from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('road.gif')
screen.title('Turtles Race')

ALIGN = "right"
FONT = ("Courier", 28, "bold")

turtles_positions_y = [-260, -172, -85, 2, 85, 172, 260]
turtles_colors = ["white", "red", "orange", "pink", "black", "blue", "yellow"]
all_turtles = []
user_bet = screen.textinput('Enter your bet.', prompt='Which turtle color? ')

for index in range(0, 7):
    the_new_turtlee = Turtle(shape="turtle")
    the_new_turtlee.shapesize(2)
    the_new_turtlee.speed('fastest')
    the_new_turtlee.penup()
    the_new_turtlee.goto(x=-350, y=turtles_positions_y[index])
    the_new_turtlee.color(turtles_colors[index])
    all_turtles.append(the_new_turtlee)

turtles_is_on = True

while turtles_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            turtles_is_on = False
            winner_turtlee = turtle.pencolor()
            if winner_turtlee == user_bet:
                print(f'You won! {winner_turtlee} turtle reached the finish. Thanks for playing!')
            else:
                print(f'You lost! The {winner_turtlee} turtle reached the finish. Thanks for playing!')
        pace_of_movement = random.randint(0, 7)
        turtle.forward(pace_of_movement)

screen.exitonclick()
