import turtle


# Functions


# Main
# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.bgpic(image)


answer_state = screen.textinput(
    title="Name a State", prompt="Enter a U.S. State name").title()

# Game
screen.mainloop()  # use screen.mainloop() or turtle.done()
