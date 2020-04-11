from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from src.fileBrowser import TelescopeNorthFileBrowser
from src.propertyHolder import propertyHolder, property_OnChangeAllowStretch


class WelcomeButton(Button):
    screenManager = ObjectProperty()

    def on_press(self, *args):
        super(WelcomeButton, self).on_press()
        self.screenManager.current = 'imageShowScreen'


class WelcomeAllowSwitchCheckbox(CheckBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active = propertyHolder.isAllowStretch

    def on_press(self):
        propertyHolder.dispatch(property_OnChangeAllowStretch, self.active)


class WelcomeButtonToFileChooser(Button):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = propertyHolder.imageFolderDir
        self.welcomeButtonToFileChooserText = propertyHolder.imageFolderDir
        self.text_size = self.width * 3, None
        propertyHolder.bind(on_changeImageFolderDir=self.changeText)

    def changeText(self, _instance, dir):
        self.text = dir

    def on_press(self):
        self.screenManager.current = 'fileChooserScreen'


class WelcomeScreenLayout(GridLayout):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(self.createAllowSwitchLayout())
        self.add_widget(self.createFileChooserLayout())
        self.add_widget(WelcomeButton(screenManager=self.screenManager, text='Start Imageshow'))

    def createAllowSwitchLayout(self):
        boxLayout = BoxLayout()
        boxLayout.add_widget(Label(text="Allow Stretch"))
        boxLayout.add_widget(WelcomeAllowSwitchCheckbox())
        return boxLayout

    def createFileChooserLayout(self):
        boxLayout = BoxLayout()
        boxLayout.add_widget(Label(text="Choose Folder"))
        boxLayout.add_widget(WelcomeButtonToFileChooser(screenManager=self.screenManager))
        return boxLayout


class WelcomeScreen(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WelcomeScreenLayout(screenManager=self.screenManager))
