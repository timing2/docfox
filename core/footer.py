from core.config import Config
import flet as ft

class Footer:
    def __init__(self, page) -> None:
        config = Config.get_instance()

        self.bottom_appbar = ft.BottomAppBar(
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