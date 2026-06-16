from pathlib import Path

from win32more import List
from win32more._collections import Vector
from win32more.Microsoft.UI.Xaml import UIElement
from win32more.Microsoft.UI.Xaml.Controls import IPageOverrides, ListViewItem, Page
from win32more.Microsoft.UI.Xaml.Media.Animation import (
    ConnectedAnimationService,
    SuppressNavigationTransitionInfo,
)
from win32more.Windows.UI.Xaml.Interop import TypeKind
from win32more.winui3 import XamlClass, xaml_typename


class ConnectedAnimationPage(XamlClass, Page):
    items = None

    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

        ConnectedAnimationPage.items = List(
            [
                {"Title": "item1", "ImageLocation": "image1.png", "Views": 463, "Likes": 33, "Description": "hogehoge"},
                {
                    "Title": "item2",
                    "ImageLocation": "image1.png",
                    "Views": 1024,
                    "Likes": 16,
                    "Description": "fugafuga",
                },
            ]
        )

        self.Frame1.Navigate(xaml_typename("winuitest.connectedanimationpage.CollectionPage", TypeKind.Custom))


class CollectionPage(XamlClass, Page):
    xaml = """<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <StackPanel Orientation="Vertical">
        <TextBlock>A connected animation between a list page and a detail page</TextBlock>
        <ListView x:Name="collection" ItemsSource="{Binding}" IsItemClickEnabled="True" Loaded="collection_Loaded" ItemClick="collection_ItemClick">
            <ListView.ItemTemplate>
                <DataTemplate>
                    <Grid>
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="Auto" MinWidth="150" />
                            <ColumnDefinition Width="*" />
                        </Grid.ColumnDefinitions>

                        <Image x:Name="connectedElement" Source="{Binding ImageLocation}" MaxHeight="100" Stretch="Fill" />

                        <StackPanel Grid.Column="1">
                            <TextBlock Text="{Binding Title}" />
                            <StackPanel Orientation="Horizontal">
                                <TextBlock Text="Views:" />
                                <TextBlock Text="{Binding Views}" />
                            </StackPanel>
                            <StackPanel Orientation="Horizontal">
                                <TextBlock Text="Likes:" />
                                <TextBlock Text="{Binding Likes}" />
                            </StackPanel>
                            <TextBlock Text="{Binding Description}" />
                        </StackPanel>
                    </Grid>
                </DataTemplate>
            </ListView.ItemTemplate>
        </ListView>
    </StackPanel>
</Page>
"""

    _storeditem = None

    def __init__(self):
        super().__init__()
        self.DataContext = ConnectedAnimationPage.items
        self.LoadComponentFromString(self.xaml, Path(__file__).with_name("connectedanimationpage_connectionpage.xaml"))

    async def collection_Loaded(self, sender, e):
        if CollectionPage._storeditem:
            animation = ConnectedAnimationService.GetForCurrentView().GetAnimation("BackConnectedAnimation")
            if animation:
                await self.collection.TryStartConnectedAnimationAsync(
                    animation, CollectionPage._storeditem, "connectedElement"
                )

    def collection_ItemClick(self, sender, e):
        container = self.collection.ContainerFromItem(e.ClickedItem).try_as(ListViewItem)
        if container:
            CollectionPage._storeditem = container.Content
            self.collection.PrepareConnectedAnimation(
                "ForwardConnectedAnimation", CollectionPage._storeditem, "connectedElement"
            )

        self.Frame.NavigateWithTransitionInfo(
            xaml_typename("winuitest.connectedanimationpage.DetailedInfoPage", TypeKind.Custom),
            CollectionPage._storeditem,
            SuppressNavigationTransitionInfo(),
        )


class DetailedInfoPage(XamlClass, Page, IPageOverrides):
    xaml = """<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <StackPanel Orientation="Vertical">
        <Button Content="Go Back" Click="BackButton_Click" />
        <TextBlock>DetailedInfoPage</TextBlock>
        <Image x:Name="detailedImage" Source="image1.png" MaxHeight="200" />
        <StackPanel x:Name="coordinatedPanel">
        </StackPanel>
    </StackPanel>
</Page>
"""

    def __init__(self):
        super().__init__()
        self.LoadComponentFromString(
            self.xaml, Path(__file__).with_name("connectedanimationpage_detailedinfopage.xaml")
        )

    def OnNavigatedFrom(self, e):
        self._inner.as_(IPageOverrides).OnNavigatedFrom(e)

    def OnNavigatedTo(self, e):
        self._inner.as_(IPageOverrides).OnNavigatedTo(e)

        imageAnimation = ConnectedAnimationService.GetForCurrentView().GetAnimation("ForwardConnectedAnimation")
        if imageAnimation:
            imageAnimation.TryStartWithCoordinatedElements(
                self.detailedImage, Vector[UIElement]([self.coordinatedPanel])
            )

    def OnNavigatingFrom(self, e):
        self._inner.as_(IPageOverrides).OnNavigatingFrom(e)

        ConnectedAnimationService.GetForCurrentView().PrepareToAnimate("BackConnectedAnimation", self.detailedImage)

    def BackButton_Click(self, sender, e):
        self.Frame.GoBack()
