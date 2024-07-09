from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class Hello(App):
  def build(self):
    self.window = GridLayout()
    self.window.cols = 1
    
    self.window.add_widget(Image(source = 'logo.png'))
    
    self.greetings = Label(text = 'what is your name?', font_size = 36, color = 'green')
    self.window.add_widget(self.greetings)
    
    self.user_Input = TextInput(multiline = False, padding_y = (20, 20))
    self.window.add_widget(self.user_Input)
    
    self.enter_Input = Button(text = 'Greet', color = 'black', background_color = 'white', bold = True, font_size = 40)
    self.window.add_widget(self.enter_Input)
    return self.window
    
Hello().run()
