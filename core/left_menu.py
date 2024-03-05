from core.config import Config
import flet as ft

class LeftMenu:
    def __init__(self) -> None:
        # Access the singleton instance of the configuration
        self.config = Config.get_instance()

        # Initialize the left menu with its components
        self.left_menu = self._initialize_left_menu()

    def _initialize_left_menu(self):
        # Define the text buttons and sections for the left bar
        items = [
            ft.Text("Introduction", size=self.config.appbar_text_size),
            ft.TextButton("Get started", disabled=True),
            ft.TextButton("Requirements"),
            ft.Divider(height=10, thickness=0, opacity=0),  # Spacing between sections
            ft.Text("Usage", size=self.config.appbar_text_size),
            ft.TextButton("Pages"),
            ft.TextButton("Docs"),
            ft.Divider(height=10, thickness=0, opacity=0),  # Spacing between sections
            ft.Text("External links", size=self.config.appbar_text_size),
            ft.TextButton("Github", icon="link", url="https://github.com/timing2/docvamp", url_target="_blank"),
            ft.TextButton("Flet", icon="link", url="https://flet.dev/docs/", url_target="_blank"),
        ]

        return ft.Column(
            items,
            spacing=5,
            width=self.config.leftbar_width,
            expand=False,
            alignment="start",
            scroll="auto",
            animate_size=ft.animation.Animation(250, ft.AnimationCurve.DECELERATE),
        )
