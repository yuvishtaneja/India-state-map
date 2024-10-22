import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
image = "India_state_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("Indian_state_data.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 36:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/36 States Correct",
                                    prompt="What's another states name").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
