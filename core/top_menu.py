from core.config import Config
import flet as ft

class TopMenu:
    def __init__(self, toggledarklight) -> None:
        # Access the singleton instance of the configuration
        self.config = Config.get_instance()

        # Create a row for the top menu using the alignment specified in the configuration
        self.top_menu = ft.Row(
            alignment=self.config.menu_alignment,
            controls=self._create_menu_controls()
        )

        self.appbar = ft.AppBar(
            toolbar_height=self.config.appbar_height,
            leading=ft.Image(src=f"logo.png") , 
            title=self.top_menu,
            leading_width=self.config.logo_width,        
            center_title=False,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            actions=[toggledarklight] 
        )

    def _create_menu_controls(self):
        # List of menu items; can be dynamically fetched or modified as needed
        menu_items = [self.config.docs_button_text, "Page 1", "Page 2"]

        # Generate text buttons for each menu item using configurations for text size
        return [
            ft.TextButton(
                content=ft.Text(value=item, size=self.config.appbar_text_size)
            ) for item in menu_items
        ]


