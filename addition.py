from kivy.app import App
from kivyMD.app import MDApp
from kivy.uix.wideget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
import random

# set the app size
Window.size = (360, 640)

# designate our .kv design file
Builder.load_file('addition.kv')

# choses two random numbers between 1 and 9 and adds them together
class MyLayout(Widget):
    def generate(self):
        # generate two random numbers between 1 and 9
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)

        # set the text of the labels to the random numbers
        self.ids.num1.text = str(num1)
        self.ids.num2.text = str(num2)

        # set the answer property to the sum of the two numbers
        self.answer = num1 + num2

    def check_answer(self, user_answer):
        # check if the user's answer is correct
        if int(user_answer) == self.answer:
            # if it is, change the label to "Correct!"
            self.ids.answer.text = "Correct!"
        else:
            # if it is not, change the label to "Incorrect!"
            self.ids.answer.text = "Incorrect!"
