from core.config import Config
import flet as ft

class LeftMenu:
    def __init__(self) -> None:
        self.config = Config.get_instance()

        self.left_menu = self._initialize_left_menu()

        v_devider = ft.Container(
                bgcolor="#666666",
                expand=True,
                width=1,                                
                padding=0,
                opacity=0.3
            )

        self.sidebar_spacer =  ft.Column(
            [
                v_devider,
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK_IOS_ROUNDED, 
                    selected_icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
                    icon_color="#666666",
                    selected_icon_color="#666666",
                    opacity=0.8,
                    on_click=self.toggle_sidebar
                    ),
                v_devider
            ],                        
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment="center",
            expand=False
        )

    def _initialize_left_menu(self):
        items = [
            ft.Text("Introduction", size=self.config.appbar_text_size),
            ft.TextButton("Get started", disabled=True),
            ft.TextButton("Requirements"),
            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("Usage", size=self.config.appbar_text_size),
            ft.TextButton("Pages"),
            ft.TextButton("Docs"),
            ft.Divider(height=10, thickness=0, opacity=0),
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

    def toggle_sidebar(self, e):        
        e.control.selected = not e.control.selected
        self.left_menu.width = 0 if e.control.selected else self.config.leftbar_width
        self.left_menu.scroll = None if e.control.selected else "auto"
        self.left_menu.update()
        e.control.update()