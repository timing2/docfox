import flet as ft

md1 = """
Installation
------------

Be aware, the installation needs technical skills and is not for beginners. Please do not open platform and installation related issues on GitHub. We have a very helpful [Discord](https://join.facefusion.io) community that will guide you to complete the installation.

Get started with the [installation](https://docs.facefusion.io/installation) guide.


Usage
-----

Run the command:

```
python run.py [options]

options:
  -h, --help                                                                                                         show this help message and exit
  -s SOURCE_PATHS, --source SOURCE_PATHS                                                                             select a source image
  -t TARGET_PATH, --target TARGET_PATH                                                                               select a target image or video
  -o OUTPUT_PATH, --output OUTPUT_PATH                                                                               specify the output file or directory
  -v, --version                                                                                                      show program's version number and exit
```
"""


def main(page: ft.Page):
    page.theme_mode = "light"
    page.scroll = "auto"
    page.add(ft.Image(src=f"/assets/icon.png"))
    page.add(ft.SafeArea(ft.Text("Hello, DocVamp!")))
    page.add(
        ft.Markdown(
            md1,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        )
    )

# run app
ft.app(
    main, 
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER)
