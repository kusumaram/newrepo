from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# create 3 squares to represent a snake body and put them in the center of the screen
segments = list()
starting_position = [(0, 0), (-20, 0), (-40,0)]
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

# move the snake
is_game_on = True
while is_game_on:
    for seg in segments:
        seg.forward(20)

















screen.exitonclick()