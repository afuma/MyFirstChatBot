#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Code to demonstrate the different events that can be done with the multiexpressionbutton object.
"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import multiexpressionbutton as meb

__author__ = "Mark Rauch Richards"


class MainWindow(GridLayout):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 1
        button = meb.MultiExpressionButton(text="Click ME")
        button.bind(on_long_press=self.long_action)
        button.bind(on_single_press=self.single_action)
        button.bind(on_double_press=self.double_action)
        self.add_widget(button)

    @staticmethod
    def long_action(instance):
        print('long press')

    @staticmethod
    def single_action(instance):
        print('single press')

    @staticmethod
    def double_action(instance):
        print('double press')


class Test(App):
    def build(self):
        self.title = 'Test'
        main = MainWindow()
        return main


if __name__ == '__main__':
    Test().run()