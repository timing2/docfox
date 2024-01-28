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
logo_width = config['appbar']['logo_width']
appbar_height = config['appbar']['appbar_height']
menu_alignment = config['appbar']['menu_alignment']
appbar_text_size = config['appbar']['appbar_text_size']
leftbar_width = config['leftbar']['leftbar_width']
footer_text = config['footer']['footer_text']
footer_text_size = config['footer']['footer_text_size']
footer_alignment = config['footer']['footer_alignment']
footer_height = config['footer']['footer_height']
font_color = ft.colors.INVERSE_SURFACE


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM

    def changetheme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        #page.update()
        # CHANGE THE ICON DARK MODE OR LIGHT MODE
        toggledarklight.selected = not toggledarklight.selected
        # AND PAGE UPDATE FOR CHANGE STATE
        page.update() 

    toggledarklight = ft.IconButton(
        on_click=changetheme,
        icon="NIGHTLIGHT_OUTLINED" if page.theme_mode == ft.ThemeMode.DARK else "LIGHT_MODE_OUTLINED",
        selected_icon="LIGHT_MODE_OUTLINED" if page.theme_mode == ft.ThemeMode.DARK else "NIGHTLIGHT_OUTLINED", 
        )

    menu = ft.Row(
        alignment=menu_alignment,
        controls=[
            ft.TextButton(content=ft.Text(value="Documentation", size=appbar_text_size)),
            ft.TextButton(content=ft.Text(value="Page 1", size=appbar_text_size)),
            ft.TextButton(content=ft.Text(value="Page 2", size=appbar_text_size)),
        ]
    )


    page.appbar = ft.AppBar(
        toolbar_height=appbar_height,
        leading=ft.Image(src=f"icon.png"), 
        title=menu,
        leading_width=logo_width,        
        center_title=False,
        bgcolor=ft.colors.ON_INVERSE_SURFACE,
        actions=[toggledarklight] 
    )


    left_bar = ft.Column([
            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("Introduction", size=appbar_text_size, color=font_color),
            ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Get started"),   
            ft.TextButton("Requirements"),

            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("Usage", size=appbar_text_size, color=font_color),
            ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Pages"),   
            ft.TextButton("Documentation"),

            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("External links", size=appbar_text_size, color=font_color),
            ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Github", icon="link", url="https://github.com/timing2/docvamp", url_target="_blank"),   
            ft.TextButton("Flet", icon="link", url="https://flet.dev/docs/", url_target="_blank"),
        ],
        spacing=5,
        width=leftbar_width,
        expand=False,
        alignment="start",
        scroll="auto"
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
    
    page.bottom_appbar = ft.BottomAppBar(
        height=footer_height,
        bgcolor=ft.colors.ON_INVERSE_SURFACE,
        content=ft.Row(
            alignment=footer_alignment,
            controls=[
                ft.Text(footer_text, size=footer_text_size),
            ]
        ),
    )


    # code_textfield
    codeblock = ft.TextField(
        text_size = 14,
        read_only=True,
        bgcolor="#161B22",
        color="white",
        content_padding=10,
        multiline=True,
        disabled=False,
        value="""
import flet
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )

flet.app(target=main)""",
            )

    
    page.add(
        ft.Row(
            [
                left_bar,
                ft.VerticalDivider(width=1),
                ft.Column([
                        markdown,
                        codeblock,
                        markdown
                    ], 
                    alignment=ft.MainAxisAlignment.START, 
                    expand=True,
                    scroll="auto"
                ),
            ],
            expand=True,
            vertical_alignment="start",

        )
    )

# run app
ft.app(
    main, 
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER)
