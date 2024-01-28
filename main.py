from pathlib import Path
import flet as ft

import configparser

""" Root path """
root_path = Path(__file__).resolve().parent


""" Config file """
# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read(root_path / 'config.ini')

# Accessing values from the 'DEFAULT' section
logo_width = config['appbar']['logo_width']
menu_alignment = config['appbar']['menu_alignment']
""" """  """ """ 

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

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


    menu = ft.Row(
        alignment=menu_alignment,
        controls=[
            ft.TextButton(content=ft.Text(value="Documentation", size=16)),
            ft.TextButton(content=ft.Text(value="Page 1", size=16)),
            ft.TextButton(
                content=ft.Text(value="GitHub", size=16),
                url="https://github.com/timing2/docvamp",
                url_target="_blank"
            ),
        ]
    )

 
    page.appbar = ft.AppBar(
        toolbar_height=60,
        leading=ft.Image(src=f"icon.png"),
        title=menu,
        leading_width=logo_width,        
        center_title=False,
        bgcolor=ft.colors.ON_INVERSE_SURFACE,
        actions=[toggledarklight] 
    )


    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    md_file = root_path / "documentation" / "Markdownexample.md"
    with open(md_file, "r", encoding="utf-8") as f:
        md1 = f.read()
    markdown = ft.Markdown(
            md1,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([
                        ft.Image(src=f"icon.png"),
                        markdown
                    ], 
                    alignment=ft.MainAxisAlignment.START, 
                    expand=True,
                    scroll="auto"
                ),
            ],
            expand=True,
        )
    )

# run app
ft.app(
    main, 
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER)
