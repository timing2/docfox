from pathlib import Path
import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"

    def changetheme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        #page.update()
        # CHANGE THE ICON DARK MODE OR LIGHT MODE
        toggledarklight.selected = not toggledarklight.selected
        # AND PAGE UPDATE FOR CHANGE STATE
        page.update() 

    toggledarklight = ft.IconButton(
        on_click=changetheme,
        icon="LIGHT_MODE_OUTLINED",
        selected_icon="NIGHTLIGHT_OUTLINED",
        icon_color="#222222",
        selected_icon_color="#eeeeee"
        )

    page.appbar = ft.AppBar(
        toolbar_height=60,
        leading=ft.Image(src=f"icon.png"),
        leading_width=80,
        title=ft.TextButton(text="Text button"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[toggledarklight],
    )


    page.add(ft.Image(src=f"icon.png", width=100))

# run app
ft.app(
    main, 
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER)
