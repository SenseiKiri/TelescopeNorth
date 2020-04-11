from boltons import fileutils
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from src.propertyHolder import propertyHolder


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


class TelescopeNorthImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_stretch = propertyHolder.isAllowStretch
        propertyHolder.bind(on_changeAllowStretch=self.changeAllow)

    def changeAllow(self, _instance, allowStretch):
        self.allow_stretch = allowStretch


class ImageShowScreenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.imageWidgetList = []
        self.createListOfImageWidgets()
        self.counter = 0
        # This property shows the object-image which is currently visible
        self.currentShowedImage = None
        Clock.schedule_interval(self.scheduledImageChange, 1)
        Clock.schedule_interval(self.scheduledNewImageLoader, 10)

    def createListOfImageWidgets(self):
        # Create a new WidgetList
        newImageWidgetList = []
        imagePathList = self.getAllImagesFromFolder()
        for imagePath in imagePathList:
            newImageWidgetList.append(
                TelescopeNorthImage(source=imagePath, keep_ratio=False))

        self.imageWidgetList = newImageWidgetList

    def scheduledImageChange(self, dt):
        self.takeNewPic()

    def scheduledNewImageLoader(self, dt):
        self.createListOfImageWidgets()

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

    def getAllImagesFromFolder(self):
        """
        This method will return all PNG/JPG/JPEG Images in Folder
            ./resources/exampleImages/
        :return: List of filepath-strings
        """
        filePath = propertyHolder.imageFolderDir
        fileGenerator = fileutils.iter_find_files(filePath, patterns=['*.png', '*jpg', '*jpeg'])
        fileList = []
        for file in fileGenerator:
            fileList.append(file)
        return fileList


class ImageShowScreen(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ImageShowScreenLayout())
        Window.bind(on_keyboard=self._on_keyboard_handler)

    def _on_keyboard_handler(self, instance, key, scancode, codepoint, modifiers):
        print(key)
        print(modifiers)
        if key == 8:
            print('works')
            self.screenManager.current = 'welcomeScreen'
