import flet as ft

class Routing:
    def __init__(self, page, left_menu, sidebar_spacer) -> None:
        self.page = page
        self.left_menu = left_menu
        self.sidebar_spacer = sidebar_spacer

    def route_change(self, e: ft.RouteChangeEvent):
        if self.page.route == "/":
            self.left_menu.visible = True
            self.sidebar_spacer.visible = True
        else:
            self.left_menu.visible = False
            self.sidebar_spacer.visible = False
        self.page.update()