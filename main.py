from pathlib import Path
import flet as ft

import configparser

""" Root path """
root_path = Path(__file__).resolve().parent


""" Config file """
# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file 
config.read(root_path / 'config.ini', encoding='utf-8')
logo_width = config['top_bar']['logo_width']
appbar_height = config['top_bar']['top_bar_height']
menu_alignment = config['top_bar']['menu_alignment']
appbar_text_size = config['top_bar']['top_bar_text_size']
docs_button_text = config['top_bar']['docs_button_text']
leftbar_width = config['general']['leftbar_width']
max_content_width = config['general']['max_content_width']
footer_text = config['footer']['footer_text']
footer_alignment = config['footer']['footer_alignment']
footer_height = config['footer']['footer_height']
font_color = ft.colors.INVERSE_SURFACE


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM

    # content spacing 
    left_content_spacer = ft.Container()
    right_content_spacer = ft.Container()

    def adjust_content_spacing(width):
        total_content_width = int(leftbar_width) + int(max_content_width)
        print('Content width:', total_content_width)
        if width < total_content_width + 50:
            left_spacer = 0
            right_spacer = 0
        else:
            total_spacer = width - total_content_width

            right_spacer = (total_spacer + int(leftbar_width)) / 2
            left_spacer = right_spacer - int(leftbar_width)

        left_content_spacer.width = left_spacer
        right_content_spacer.width = right_spacer
        page.update()
    
    adjust_content_spacing(page.window_width)
    def page_resize(e):
        print("New page width:", page.window_width)
        adjust_content_spacing(page.window_width)       

    page.on_resize = page_resize 


    # Change theme
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


    # Top bar
    menu = ft.Row(
        alignment=menu_alignment,
        controls=[
            ft.TextButton(content=ft.Text(value=docs_button_text, size=appbar_text_size)),
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


    # Left bar
    left_bar = ft.Column([
            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("Introduction", size=appbar_text_size, color=font_color),
            #ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Get started"),   
            ft.TextButton("Requirements"),

            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("Usage", size=appbar_text_size, color=font_color),
            #ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Pages"),   
            ft.TextButton("Docs"),

            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("External links", size=appbar_text_size, color=font_color),
            #ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Github", icon="link", url="https://github.com/timing2/docvamp", url_target="_blank"),   
            ft.TextButton("Flet", icon="link", url="https://flet.dev/docs/", url_target="_blank"),
        ],
        spacing=5,
        width=leftbar_width, 
        expand=False,
        alignment="start",
        scroll="always",
    )

    # MD content (need to edit)
    md_file = root_path / "documentation" / "Markdownexample.md"
    with open(md_file, "r", encoding="utf-8") as f:
        md1 = f.read()
    markdown = ft.Markdown(
            md1,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        )
    

    # Footer
    page.bottom_appbar = ft.BottomAppBar(
        height=footer_height,
        bgcolor=ft.colors.ON_INVERSE_SURFACE,
        content=ft.Row(
            alignment=footer_alignment,
            controls=[
                ft.Markdown(
                    footer_text,
                    selectable=True,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    on_tap_link=lambda e: page.launch_url(e.data),
                )
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

    # Add content to page
    page.add(
            ft.Row(
                [
                    left_bar,
                    ft.VerticalDivider(width=1, opacity=0.3),
                    left_content_spacer,                         
                    ft.Column([
                            markdown,
                            codeblock,
                            markdown
                        ], 
                        alignment=ft.MainAxisAlignment.START, 
                        expand=True,
                        scroll="auto",
                    ),  
                    right_content_spacer,                     
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
