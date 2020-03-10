from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class WelcomeButton(Button):
    screenManager = ObjectProperty()

    def on_press(self, *args):
        super(WelcomeButton, self).on_press()
        self.screenManager.current = 'imageShowScreen'


class WelcomeScreenLayout(BoxLayout):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeButton(screenManager=self.screenManager))


class WelcomeScreen(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeScreenLayout(screenManager=self.screenManager))
