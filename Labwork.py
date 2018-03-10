# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
import numpy as np
import random as rd
import re

# loading kivy file
Builder.load_file('base_1.kv')

# config settings for window
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 700)
Config.set('graphics', 'height', 500)


class RootWidget(Widget):

    def count(self, action):
        # We're passing action parameter to define what action will be implemented
        # Variables a and b are sets generated
        # from strings of input widgets using split() method.
        a = set(i for i in self.ids.a_set.text.split())
        b = set(i for i in self.ids.b_set.text.split())

        # actions is a dictionary with all basic actions with sets
        actions = {
            "unity": set.union(a, b),
            "intersection": set.intersection(a, b),
            "difference_a": set.difference(a, b),
            "difference_b": set.difference(b, a),
            "symmetric_difference": set.symmetric_difference(a, b),
        }
        # self.ids is used to get the dictionary of widget IDs
        # result_field - id of Label widget
        # text attribute is used to get or set value of string inside widget
        # join() method returns a string concatenated with elements of iterable
        # sorted() function return a list sorted by key parameter
        self.ids.result_field.text = ' '.join(i for i in sorted(actions[action], key=self.natural_keys))

    # natural sort
    def atoi(self, text):
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):
        return [self.atoi(c) for c in re.split('(\d+)', text)]

    def clear(self, instance):
        # clear input and result widgets
        self.ids.a_set.text = ""
        self.ids.b_set.text = ""
        self.ids.result_field.text = " "

    # generates random lists and converts into sets
    # for following operations with it
    def rand_set(self, instance):
        a_ = set(np.random.randint(20, size=rd.randint(10, 30)))
        b_ = set(np.random.randint(20, size=rd.randint(10, 30)))
        self.ids.a_set.text = " ".join(str(i) for i in b_)
        self.ids.b_set.text = " ".join(str(i) for i in a_)


class MyApp(App):

    title = "Set theory" # title of app

    def build(self):
        return RootWidget()

# running app
if __name__ == "__main__":
    MyApp().run()
