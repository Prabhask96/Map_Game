from turtle import Turtle, Screen
import pandas
screen = Screen()
turtle_1 = Turtle()

screen.setup(width=600, height=800)
screen.title("India's State game")
img = "Indian_map.gif"
screen.addshape(img)
turtle_1.shape(img)
game_on = True
data = pandas.read_csv("indian_states.csv")
all_states = data["state"].to_list()

guess_states = []

while len(guess_states) <= 30:

    ans_states = screen.textinput(title=f"{len(guess_states)}/30", prompt="What's another state's name").title()


    if ans_states == "Exit":
        not_guess_state = []
        for states in all_states:
            if states not in guess_states:
                not_guess_state.append(states)
        new_data = pandas.DataFrame(not_guess_state)
        new_data.to_csv("Learn_this_states.csv")
        break


    if ans_states in all_states:
        guess_states.append(ans_states)
        turtle_2 = Turtle()
        turtle_2.penup()
        turtle_2.hideturtle()
        state_data = data[data.state == ans_states]
        turtle_2.goto(x=int(state_data.x), y=int(state_data.y))
        turtle_2.write(ans_states)






