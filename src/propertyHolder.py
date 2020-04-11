from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty, StringProperty

property_OnChangeAllowStretch = 'on_changeAllowStretch'
property_OnChangeImageFolderDir = 'on_changeImageFolderDir'

class PropertyHolder(EventDispatcher):
    isAllowStretch = BooleanProperty(True)
    imageFolderDir = StringProperty('')

    def __init__(self, **kwargs):
        self.register_event_type(property_OnChangeAllowStretch)
        self.register_event_type(property_OnChangeImageFolderDir)
        super(PropertyHolder, self).__init__(**kwargs)

    def on_changeAllowStretch(self, allowStretch):
        self.isAllowStretch = allowStretch
        print('Change on_changeAllowStretch to {}'.format(allowStretch))

    def on_changeImageFolderDir(self, imageFolderDir):
        print('Change imageFolderDir from {} to {}'.format(self.imageFolderDir, imageFolderDir))
        self.imageFolderDir = imageFolderDir


propertyHolder = PropertyHolder()
