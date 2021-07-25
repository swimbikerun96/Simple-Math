import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import simplemath as sm

#Connect my python code to the front end .kv file
Builder.load_file('math_frontend.kv')
class Grid(Widget):

    def math(self):
        #assign inputs to variables, run them through the simplemath function, and then add them to the output label
        firstNumber = self.ids.firstNumber.text
        secondNumber = self.ids.secondNumber.text
        output = sm.simpleMath(firstNumber, secondNumber)
        self.ids.output.text = output

    def segue1(self):
        #focuses on the second text input while turning text in the first input green
        self.ids.firstNumber.foreground_color = "#00ff04"
        self.ids.secondNumber.focus = True
        self.ids.secondNumber.foreground_color = "#000000"

    def segue2(self):
        #focuses on the first text input while turning text in the second input green
        self.ids.secondNumber.foreground_color = "#00ff04"
        self.ids.firstNumber.focus = True
        self.ids.firstNumber.foreground_color = "#000000"
        

class MyApp(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    MyApp().run()
