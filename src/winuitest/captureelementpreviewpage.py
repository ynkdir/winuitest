from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Windows.Media.Capture import (
    MediaCapture,
    MediaCaptureInitializationSettings,
    MediaCaptureMemoryPreference,
    MediaCaptureSharingMode,
    StreamingCaptureMode,
)
from win32more.Windows.Media.Capture.Frames import MediaFrameSourceGroup
from win32more.Windows.Media.Core import MediaSource
from win32more.xaml import XamlClass


class CaptureElementPreviewPage(XamlClass, Page):
    def __init__(self):
        self._media_capture = None
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    async def _Loaded(self, sender, args):
        await self._start_capture_element()

    async def _start_capture_element(self):
        groups = await MediaFrameSourceGroup.FindAllAsync()
        if len(groups) == 0:
            self.Output.Text = "No camera devices found."
            return
        media_frame_source_group = groups[0]

        self.Output.Text = "Viewing: " + media_frame_source_group.DisplayName
        self._media_capture = MediaCapture()
        settings = MediaCaptureInitializationSettings()
        settings.SourceGroup = media_frame_source_group
        settings.SharingMode = MediaCaptureSharingMode.SharedReadOnly
        settings.StreamingCaptureMode = StreamingCaptureMode.Video
        settings.MemoryPreference = MediaCaptureMemoryPreference.Cpu
        await self._media_capture.InitializeWithSettingsAsync(settings)

        frame_source = self._media_capture.FrameSources[media_frame_source_group.SourceInfos[0].Id]
        self.captureElement.Source = MediaSource.CreateFromMediaFrameSource(frame_source)
