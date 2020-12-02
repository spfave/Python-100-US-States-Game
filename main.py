import turtle
import pandas as pd

# Functions


# Main
# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.bgpic(image)

state_data = pd.read_csv("./us-states-game-start/50_states.csv")
print(state_data.state.values)

answer_state = screen.textinput(
    title="Name a State", prompt="Enter a U.S. State name").title()

if answer_state in state_data.state.values:
    print("correct")

# Game
screen.mainloop()  # use screen.mainloop() or turtle.done()
