import turtle
import pandas as pd


# Constants
NUM_STATES = 50


# Functions


# Main
# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.bgpic(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

us_state_data = pd.read_csv("./us-states-game-start/50_states.csv")
score = 0
guessed_states = []


# Game
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{score}/{NUM_STATES} States Correct", prompt="Enter a U.S. State name").title()

    if answer_state in us_state_data.state.values:
        state_data = us_state_data[us_state_data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
        guessed_states.append(answer_state)


screen.mainloop()  # use screen.mainloop() or turtle.done()
