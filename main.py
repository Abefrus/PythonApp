from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class FirstScreen(Screen):

  def __init__(self, name="first"):
    super().__init__(name=name)
    btn = Button(text="First button!")
    btn.on_press = self.main
    lable = Label(text="This is first screen")

    self.add_widget(btn)

  def main(self):
    self.manager.transition.direction = "up"
    self.manager.current = "main"


class SecoundScreen(Screen):

  def __init__(self, name="second"):
    super().__init__(name=name)
    btn = Button(text="Second button!")
    btn.on_press = self.main
    self.add_widget(btn)

  def main(self):
    self.manager.transition.direction = "down"
    self.manager.current = "main"


class ThirdScreen(Screen):

  def __init__(self, name="third"):
    super().__init__(name=name)
    btn = Button(text="Third button!")
    btn.on_press = self.main
    self.add_widget(btn)

  def main(self):
    self.manager.transition.direction = "left"
    self.manager.current = "main"


class FourScreen(Screen):

  def __init__(self, name="four"):
    super().__init__(name=name)
    btn = Button(text="Four button!")
    btn.on_press = self.main
    self.add_widget(btn)

  def main(self):
    self.manager.transition.direction = "right"
    self.manager.current = "second"


class MainScreen(Screen):

  def __init__(self, name="main"):
    super().__init__(name=name)
    layout = BoxLayout(orientation="vertical")
    btnf = Button(text="Go to first screen")
    btnf.on_press = self.first
    layout.add_widget(btnf)

    btns = Button(text="Go to first screen")
    btns.on_press = self.second
    layout.add_widget(btns)

    btnt = Button(text="Go to first screen")
    btnt.on_press = self.third
    layout.add_widget(btnt)

    btnff = Button(text="Go to first screen")
    btnff.on_press = self.four
    layout.add_widget(btnff)

    self.add_widget(layout)

  def first(self):
    self.manager.transition.direction = "right"
    self.manager.current = "first"

  def second(self):
    self.manager.transition.direction = "right"
    self.manager.current = "second"

  def third(self):
    self.manager.transition.direction = "right"
    self.manager.current = "third"

  def four(self):
    self.manager.transition.direction = "right"
    self.manager.current = "four"


class MyApp(App):

  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainScreen())
    sm.add_widget(FirstScreen())
    sm.add_widget(SecoundScreen())
    sm.add_widget(ThirdScreen())
    sm.add_widget(FourScreen())
    return sm


MyApp().run()
