import os
import json
from interface import App
from bot_brain import Bot_Brain

switch_on = False
user_input = App().main_app()
switch_on = True

with open('user_info.json', 'r') as file:
    data = json.load(file)

if switch_on:
    app = Bot_Brain()
    # app.login(os.getenv("CGMAIL"), os.getenv("PASSWORD"))
    app.login(data['email'], data['password'])
    app.engine(user_input[0], user_input[1])

