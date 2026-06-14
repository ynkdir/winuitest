from datetime import timedelta
from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Microsoft.UI.Xaml.Media import CompositionTarget
from win32more.Windows.Foundation.Numerics import Vector3
from win32more.winui3 import XamlClass


class AnimationInteropPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

        self._compositor = CompositionTarget.GetCompositorForCurrentThread()
        self._spring_animation = self._compositor.CreateSpringVector3Animation()
        self._spring_animation.Target = "Scale"

    def update_spring_animation(self, final_value: float):
        self._spring_animation.FinalValue = Vector3(final_value, final_value, 1)
        self._spring_animation.DampingRatio = 0.6
        self._spring_animation.Period = timedelta(seconds=0.3)

    def Button1_PointerEntered(self, sender, args):
        self.update_spring_animation(1.5)
        self.Button1.StartAnimation(self._spring_animation)

    def Button1_PointerExited(self, sender, args):
        self.update_spring_animation(1)
        self.Button1.StartAnimation(self._spring_animation)
