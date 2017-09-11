import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label


class HelloKivy(App):
    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        return Label(text="Hello Kivy")


helloKivy = HelloKivy()
helloKivy.run()