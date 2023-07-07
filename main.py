import turtle
import pandas 

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State", prompt="What's another states name?").title()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

hash = {}

for state in all_states:
    hash[]

# if all_states[answer_state]: 
#     #put the state on the map
#     print(f'You wrote {answer_state}')