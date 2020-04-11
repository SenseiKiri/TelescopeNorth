from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooser, FileChooserListView
from kivy.uix.screenmanager import Screen

from src.propertyHolder import propertyHolder, property_OnChangeImageFolderDir


class TelescopeNorthFileBrowser(FileChooserListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dirselect = True
        self.path = '~'

    def on_submit(self, selected, touch=None):
        propertyHolder.dispatch(property_OnChangeImageFolderDir, selected)

    def entry_touched(self, entry, touch):
        super().entry_touched(entry, touch)
        propertyHolder.dispatch(property_OnChangeImageFolderDir, entry.path)


class FileChooserButtonOkToWelcomeScreen(Button):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Auswählen'

    def on_press(self):
        self.screenManager.current = 'welcomeScreen'


class FileChooserButtonCancelToWelcomeScreen(Button):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Abbrechen'

    def on_press(self):
        self.screenManager.current = 'welcomeScreen'


class FileChooserScreenLayout(BoxLayout):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(TelescopeNorthFileBrowser(size_hint=(1, 0.8)))
        self.add_widget(self.createOkCancelGroup())

    def createOkCancelGroup(self):
        boxLayout = BoxLayout(size_hint=(1, 0.2))
        boxLayout.add_widget(FileChooserButtonCancelToWelcomeScreen(screenManager=self.screenManager))
        boxLayout.add_widget(FileChooserButtonOkToWelcomeScreen(screenManager=self.screenManager))
        return boxLayout


class FileChooserScreen(Screen):
    screenManager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FileChooserScreenLayout(screenManager=self.screenManager))
