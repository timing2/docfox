from core.config import Config
import flet as ft

class TopMenu:
    def __init__(self, page) -> None:
        self.config = Config.get_instance()
        self.page = page
        self.top_menu = ft.Row(
            alignment=self.config.menu_alignment,
            controls=self._create_menu_controls()
        )

        self.toggledarklight = ft.IconButton(
            on_click=self.change_theme,
            icon="NIGHTLIGHT_OUTLINED" if page.theme_mode == ft.ThemeMode.DARK else "LIGHT_MODE_OUTLINED",
            selected_icon="LIGHT_MODE_OUTLINED" if page.theme_mode == ft.ThemeMode.DARK else "NIGHTLIGHT_OUTLINED",
        )

        self.appbar = ft.AppBar(
            toolbar_height=self.config.appbar_height,
            leading=ft.Image(src=f"logo.png") , 
            title=self.top_menu,
            leading_width=self.config.logo_width,        
            center_title=False,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            actions=[self.toggledarklight] 
        )

    def _create_menu_controls(self):
        menu_items = [self.config.docs_button_text, "Page 1", "Page 2"]

        return [
            ft.TextButton(
                content=ft.Text(value=item, size=self.config.appbar_text_size)
            ) for item in menu_items
        ]

    def change_theme(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self.toggledarklight.selected = not self.toggledarklight.selected
        self.page.update()


