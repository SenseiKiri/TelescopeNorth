from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.imageShowScreen import ImageShowScreen
from src.welcomeScreen import WelcomeScreen

sm = ScreenManager()
sm.add_widget(WelcomeScreen(screenManager=sm, name='welcomeScreen'))
sm.add_widget(ImageShowScreen(name='imageShowScreen'))


class MainApp(App):
    def build(self):
        return sm


MainApp().run()
