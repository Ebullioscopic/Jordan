from panda3d_kivy.app import App
from kivy.uix.button import Button

from direct.showbase.ShowBase import ShowBase

class Example(App):
    def build(self):
        return Button(text='Hello, world!')
    
class PandaApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.kivy_app = kivy_app = Example(self)
        kivy_app.run()

        # The rest of your ShowBase code here


app = PandaApp()
app.run()
