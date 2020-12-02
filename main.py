import turtle


# Functions
def get_mouse_click_coord(x, y):
    print(x, y)


# Main
# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.bgpic(image)

screen.onscreenclick(fun=get_mouse_click_coord)

# Game
screen.mainloop()  # use screen.mainloop() or turtle.done()
