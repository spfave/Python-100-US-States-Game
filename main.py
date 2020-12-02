import turtle
import pandas as pd

# Functions


# Main
# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.bgpic(image)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

us_state_data = pd.read_csv("./us-states-game-start/50_states.csv")


answer_state = screen.textinput(
    title="Name a State", prompt="Enter a U.S. State name").title()

if answer_state in us_state_data.state.values:
    print("correct")
    state_data = us_state_data[us_state_data.state == answer_state]
    turtle.goto(int(state_data.x), int(state_data.y))
    turtle.write(answer_state)


# Game
screen.mainloop()  # use screen.mainloop() or turtle.done()
