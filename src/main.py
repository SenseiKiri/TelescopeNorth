import kivy
from kivy.clock import Clock
from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Window.borderless = True

listOfImagePaths = [
    './resources/exampleImages/Rocket.jpg',
    './resources/exampleImages/horse.jpeg'
]

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.imageWidgetList = []
        self.createListOfImageWidgets()
        self.counter = 0

    def createListOfImageWidgets(self):
        for imagePath in listOfImagePaths:
            self.imageWidgetList.append(Image(source=imagePath))

    def takeNewPic(self):
        self.remove_widget(self.imageWidgetList[self.counter])
        self.counter = self.counter + 1
        if self.counter >= len(self.imageWidgetList):
            self.counter = 0
        self.add_widget(self.imageWidgetList[self.counter])


mainWidget = MainScreen()


def scheduledImageChange(dt):
    mainWidget.takeNewPic()

# Main Window
class TelescopeNorth(App):
    def build(self):
        event = Clock.schedule_interval(scheduledImageChange, 1)
        self.title = "Telescope North"
        return mainWidget


# Run Application
TelescopeNorth().run()
