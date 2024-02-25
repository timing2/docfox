from pathlib import Path
from core.config import Config
import flet as ft

# Access the singleton configuration instance from the Config class.
config = Config.get_instance()

# Define a font color using Flet's predefined color scheme for better UI contrast.
# INVERSE_SURFACE is typically used to ensure text is readable on contrasting backgrounds.
font_color = ft.colors.INVERSE_SURFACE







root_path = Path(__file__).resolve().parent # remove when adding from module




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
    # Access configuration instance and set up Flet page properties
    config = Config.get_instance()  # Configuration access
    page.theme_mode = ft.ThemeMode.SYSTEM  # Adapt page to system theme (light/dark)
    page.title = config.docs_page_title  # Page title from configuration
    font_color = ft.colors.INVERSE_SURFACE  # Contrast-enhancing font color for UI components

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
        toggledarklight.selected = not toggledarklight.selected
        page.update() 

    toggledarklight = ft.IconButton(
        on_click=changetheme,
        icon="NIGHTLIGHT_OUTLINED" if page.theme_mode == ft.ThemeMode.DARK else "LIGHT_MODE_OUTLINED",
        selected_icon="LIGHT_MODE_OUTLINED" if page.theme_mode == ft.ThemeMode.DARK else "NIGHTLIGHT_OUTLINED", 
        )


    # Top bar
    menu = ft.Row(
        alignment=config.menu_alignment,
        controls=[
            ft.TextButton(content=ft.Text(value=config.docs_button_text, size=config.appbar_text_size)),
            ft.TextButton(content=ft.Text(value="Page 1", size=config.appbar_text_size)),
            ft.TextButton(content=ft.Text(value="Page 2", size=config.appbar_text_size)),
        ]
    )

    page.appbar = ft.AppBar(
        toolbar_height=config.appbar_height,
        leading=ft.Image(src=f"icon.png"), 
        title=menu,
        leading_width=config.logo_width,        
        center_title=False,
        bgcolor=ft.colors.ON_INVERSE_SURFACE,
        actions=[toggledarklight] 
    )


    # Left bar
    left_bar = ft.Column([
            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("Introduction", size=config.appbar_text_size, color=font_color),
            #ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Get started",disabled=True),   
            ft.TextButton("Requirements"),

            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("Usage", size=config.appbar_text_size, color=font_color),
            #ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Pages"),   
            ft.TextButton("Docs"),

            ft.Divider(height=10, thickness=0, opacity=0),
            ft.Text("External links", size=config.appbar_text_size, color=font_color),
            #ft.Divider(height=0, thickness=2, opacity=0.3),  
            ft.TextButton("Github", icon="link", url="https://github.com/timing2/docvamp", url_target="_blank"),   
            ft.TextButton("Flet", icon="link", url="https://flet.dev/docs/", url_target="_blank"),
        ],
        spacing=5,
        width=config.leftbar_width, 
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
        height=config.footer_height,
        bgcolor=ft.colors.ON_INVERSE_SURFACE,
        content=ft.Row(
            alignment=config.footer_alignment,
            controls=[
                ft.Markdown(
                    config.footer_text,
                    selectable=True,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    on_tap_link=lambda e: page.launch_url(e.data),
                )
            ]
        ),
    )




    # Codeblock
    # Alert - Snackbar (Code copied)
    page.snack_bar = ft.SnackBar(
        content=ft.Text(config.copied_notification_text, color="#6B6B6B"),
        bgcolor="#D9D9D9",
        duration=1500        
    )

    def on_click(e):
        page.snack_bar.open = True
        page.update()

    # Copy code function
    def copy_code(code_to_copy):
        def copy_text(e):
            print("Copying:", code_to_copy)  # Debug print
            page.set_clipboard(code_to_copy)
            on_click(e)
        return copy_text

    # Codeblock-top bg= #272A2C
    codeblock_top = ft.Container(
        content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.COPY_ROUNDED,
                        icon_size=18,
                        tooltip=config.codeblock_copy_tooltip,
                        style=ft.ButtonStyle(color=config.codeblock_copy_icon_color.replace('"', '')),
                        on_click=lambda e: copy_code(sample_code)(e)
                        ),
                    ft.VerticalDivider(width=0)
                ],
                alignment= "end",
        ),
        padding=2,        
        bgcolor=config.codeblock_top_bgcolor.replace('"', ''),
        border=ft.border.only(
            top=ft.border.BorderSide(1, config.codeblock_border_color.replace('"', '')),
            right=ft.border.BorderSide(1, config.codeblock_border_color.replace('"', '')),
            left=ft.border.BorderSide(1, config.codeblock_border_color.replace('"', ''))
            ),
            border_radius=ft.border_radius.only(top_left=10, top_right=10)
    )
    
        

    # Codeblock-text field
    codeblock_text = ft.TextField(
        text_size = 14,
        read_only=True,
        bgcolor=config.codeblock_body_bgcolor.replace('"', ''),
        color=config.codeblock_text_color.replace('"', ''),
        border_radius=0,
        border_color=config.codeblock_border_color.replace('"', ''),
        border_width=0,
        content_padding=10,
        multiline=True,
        disabled=False,
        value= sample_code,
            )
    # Codeblock-column
    codeblock_container = ft.Container(
        content=ft.Column([
                codeblock_top,
                codeblock_text,
                ],
                spacing=0,
                ),
            padding=ft.padding.symmetric(vertical=20)
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
                                        codeblock_container,
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
