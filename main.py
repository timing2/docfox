from pathlib import Path
import flet as ft

import configparser

""" Root path """
root_path = Path(__file__).resolve().parent


""" Config file """
# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file 
config.read(root_path / 'settings.ini', encoding='utf-8')
leftbar_width = config['general']['leftbar_width']
docs_page_title = config['general']['docs_page_title']
logo_width = config['top_bar']['logo_width']
appbar_height = config['top_bar']['top_bar_height']
menu_alignment = config['top_bar']['menu_alignment']
appbar_text_size = config['top_bar']['top_bar_text_size']
docs_button_text = config['top_bar']['docs_button_text']
footer_text = config['footer']['footer_text']
footer_alignment = config['footer']['footer_alignment']
footer_height = config['footer']['footer_height']
codeblock_copy_tooltip = config['codeblock']['codeblock_copy_tooltip']

font_color = ft.colors.INVERSE_SURFACE


# sample MD code
sample_code = """
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

flet.app(target=main)"""




def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = docs_page_title

    #routing
    """ def route_change(e: ft.RouteChangeEvent): 
        page.add(ft.Text(f"New route: {e.route}"))

    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))
    page.route = "/docs" 
    print(page.route) """


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
            ft.TextButton("Get started",disabled=True),   
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




    # Codeblock
    # Copy code function
    def copy_code(code_to_copy):
        def copy_text(e):
            print("Copying:", code_to_copy)  # Debug print
            page.set_clipboard(code_to_copy)
        return copy_text

    # Codeblock-top bg= #272A2C
    codeblock_top = ft.Container(
        content=ft.Row(
                [   
                    ft.Text("Copy", size=12),
                    ft.IconButton(
                        icon=ft.icons.COPY_ROUNDED,
                        icon_size=20,
                        tooltip=codeblock_copy_tooltip,
                        style=ft.ButtonStyle(color={"": ft.colors.LIGHT_BLUE_ACCENT}),
                        on_click=lambda e: copy_code(sample_code)(e)
                        ),
                    ft.VerticalDivider(width=0)
                ],
                alignment="end",
        ),
        bgcolor="#272A2C",
        border=ft.border.only(
            top=ft.border.BorderSide(1, "#222222"),
            right=ft.border.BorderSide(1, "#222222"),
            left=ft.border.BorderSide(1, "#222222")
            ),
            border_radius=ft.border_radius.only(top_left=10, top_right=10)

    )
    
        

    # Codeblock-text field
    codeblock_text = ft.TextField(
        text_size = 14,
        read_only=True,
        bgcolor="#0E1114",
        color="white",
        border_radius=0,
        border_color="#222222",
        border_width=0,
        content_padding=10,
        multiline=True,
        disabled=False,
        value= sample_code,
            )
    # Codeblock-column
    codeblock = ft.Column([
        codeblock_top,
        codeblock_text
        ],
        spacing=0
    )

    # Add content to page
    page.add(
            ft.Row(
                [   
                    left_bar,
                    ft.VerticalDivider(width=1, opacity=0.3), 
                    ft.Column([
                            ft.ResponsiveRow([
                                ft.Column(col={"lg": 1, "xl": 1, "xxl": 2}),
                                ft.Column(col={"lg": 10, "xl": 8, "xxl": 6}, controls=[
                                        markdown,
                                        codeblock,
                                        markdown
                                    ]),                                
                                ft.Column(col={"lg": 1, "xl": 3, "xxl": 4}),
                            ]),                            
                        ], 
                        alignment=ft.MainAxisAlignment.START, 
                        expand=True,
                        scroll="auto",
                    ),                       
                ],
                expand=True,
                vertical_alignment="start",
                alignment="start"
                
            )
    )


# run app
ft.app(
    target=main, 
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER,
    port=5000)
