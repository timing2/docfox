from pathlib import Path
from core.config import Config
from core.top_menu import TopMenu
from core.left_menu import LeftMenu
from core.footer import Footer
from core.routing import Routing
import flet as ft

root_path = Path(__file__).resolve().parent # remove when adding from module

config = Config.get_instance()

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = config.docs_page_title

    # Display a snack bar notification on the page.
    def open_snack_bar(e):        
        page.snack_bar.open = True
        page.update()

    # Function to copy a given text to the clipboard and display a notification.
    def copy_code(code_to_copy):
        def copy_text(e):
            page.set_clipboard(code_to_copy)
            open_snack_bar(e)
        return copy_text

    # Alert - Snackbar (Code copied)
    page.snack_bar = ft.SnackBar(
        content=ft.Text(config.copied_notification_text, color="#6B6B6B"),
        bgcolor="#D9D9D9",
        duration=1500        
    )    

    # Create an instance of the TopMenu class
    top_navigation_menu = TopMenu(page) 
    page.appbar = top_navigation_menu.appbar   

    # Create an instance of the LeftMenu class
    left_navigation_menu = LeftMenu()
    left_menu = left_navigation_menu.left_menu
    sidebar_spacer = left_navigation_menu.sidebar_spacer

    # Create an instance of the Footer class
    footer = Footer(page)
    page.bottom_appbar = footer.bottom_appbar


    # Routing
    routing = Routing(page, left_menu, sidebar_spacer)
    page.on_route_change = routing.route_change


##################################### Clean from here



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

    # sample MD code
    sample_code = """import flet
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

    # Codeblock
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
        value=sample_code,
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
                    left_menu,
                    sidebar_spacer,
                    ft.Column([
                            ft.ResponsiveRow([
                                ft.Column(col={"lg": 1, "xl": 2, "xxl": 3}),
                                ft.Column(col={"lg": 10, "xl": 8, "xxl": 6}, controls=[
                                        markdown,
                                        codeblock_container,
                                        markdown
                                    ]),                                
                                ft.Column(col={"lg": 1, "xl": 2, "xxl": 3}),
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
    #port=5000
    )
