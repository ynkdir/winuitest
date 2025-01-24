from pathlib import Path

from win32more.Microsoft.UI.Xaml import ElementSoundPlayer, ElementSoundPlayerState
from win32more.Microsoft.UI.Xaml.Controls import Button, Page
from win32more.xaml import XamlClass


class SoundPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def soundToggle_Toggled(self, sender, args):
        if self.soundToggle.IsOn:
            ElementSoundPlayer.State = ElementSoundPlayerState.On
        else:
            ElementSoundPlayer.State = ElementSoundPlayerState.Off

    def Button_Click(self, sender, args):
        tagInt = int(sender.as_(Button).Tag.as_(str))
        ElementSoundPlayer.Play(tagInt)
