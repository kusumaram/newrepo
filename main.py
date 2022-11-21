import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = []
# take user input for which colored turtle is going to win
no_of_players = int(screen.numinput(title="Players", prompt="How many players: ", minval=2))
players = dict()
for _ in range(0, no_of_players):
    user_name = screen.textinput(title="Player Name", prompt="Enter your name: ")
    user_color = screen.textinput(title="Make Your Bet", prompt="choose color of your turtle? Enter a color: ")
    players[user_name] = user_color
    colors.append(user_color)
y_position = [160, 100, 40, -20, -80, -140]
all_turtles = []
for i in range(0, no_of_players):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

# until user choose a turtle the race will not start
if players:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle_color = turtle.pencolor()
            for player in players:
                if players[player] == winner_turtle_color:
                    print(f"The {winner_turtle_color} of {player.upper()} turtle win the race.")
            # else:
            #     print(f"You Lost! The {winner_turtle_color} turtle win the race.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
