import kivy
from kivy.clock import Clock
from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import src.imageFileUtils as importFileUtils

Window.borderless = True

listOfImagePaths = [
    './resources/exampleImages/rocket.txt',
    './resources/exampleImages/horse.jpeg'
]


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.imageWidgetList = []
        self.createListOfImageWidgets()
        self.counter = 0
        # This property shows the object-image which is currently visible
        self.currentShowedImage = None

    def createListOfImageWidgets(self):
        # Create a new WidgetList
        newImageWidgetList = []
        imagePathList = importFileUtils.getAllImagesFromFolder()
        for imagePath in imagePathList:
            newImageWidgetList.append(Image(source=imagePath))

        self.imageWidgetList = newImageWidgetList

    def takeNewPic(self):
        # remove current image
        if self.currentShowedImage is not None:
            self.remove_widget(self.currentShowedImage)

        # It is possible, that this list is empty
        if len(self.imageWidgetList) != 0:
            # increment counter
            self.counter = self.counter + 1
            if self.counter >= len(self.imageWidgetList):
                self.counter = 0

            # add new image
            nextImage = self.imageWidgetList[self.counter]
            self.add_widget(nextImage)
            self.currentShowedImage = nextImage


mainWidget = MainScreen()


def scheduledImageChange(dt):
    """
    This method will used for schedule showing a new image
    """
    mainWidget.takeNewPic()


def scheduledNewImageLoader(dt):
    """
    Thid method will be used for schedule to load new images
    """
    mainWidget.createListOfImageWidgets()


# Main Window
class TelescopeNorth(App):
    def build(self):
        Clock.schedule_interval(scheduledImageChange, 1)
        Clock.schedule_interval(scheduledNewImageLoader, 10)
        self.title = "Telescope North"
        return mainWidget


# Run Application
TelescopeNorth().run()
