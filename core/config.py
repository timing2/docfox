from pathlib import Path
import configparser
from datetime import datetime

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initializes the config by reading from the settings.ini file."""
        # Define the root path based on the location of this file.
        root_path = Path(__file__).resolve().parent.parent
        current_year = datetime.now().year
        config = configparser.ConfigParser()
        config.read(root_path / 'settings.ini', encoding='utf-8')

        # General configurations with checks for empty values
        self.leftbar_width = config.get('general', 'leftbar_width') or '200'
        self.docs_page_title = config.get('general', 'docs_page_title') or 'FlashDoc 🚀 Empowering Documentation'

        # Top bar configurations with checks for empty values
        self.logo_width = config.get('top_bar', 'logo_width') or '50'
        self.appbar_height = config.get('top_bar', 'top_bar_height') or '60'
        self.menu_alignment = config.get('top_bar', 'menu_alignment') or 'center'
        self.appbar_text_size = config.get('top_bar', 'top_bar_text_size') or '16'
        self.docs_button_text = config.get('top_bar', 'docs_button_text') or 'Docs'

        # Footer configurations with checks for empty values
        self.footer_text = config.get('footer', 'footer_text') or f'Copyright © {current_year} [FlashDoc](https://github.com/timing2/docvamp) 🚀 Empowering Documentation 📄'
        self.footer_alignment = config.get('footer', 'footer_alignment') or 'center'
        self.footer_height = config.get('footer', 'footer_height') or '60'

        # Codeblock configurations with checks for empty values
        self.codeblock_copy_tooltip = config.get('codeblock', 'codeblock_copy_tooltip') or 'Copy code'
        self.codeblock_top_bgcolor = config.get('codeblock', 'codeblock_top_bgcolor') or '#272A2C'
        self.codeblock_copy_icon_color = config.get('codeblock', 'codeblock_copy_icon_color') or '#FFFFFF'
        self.codeblock_body_bgcolor = config.get('codeblock', 'codeblock_body_bgcolor') or '#0E1114'
        self.codeblock_text_color = config.get('codeblock', 'codeblock_text_color') or '#FFFFFF'
        self.codeblock_border_color = config.get('codeblock', 'codeblock_border_color') or '#222222'
        self.copied_notification_text = config.get('codeblock', 'copied_notification_text') or 'Code snatched! Now chilling on your clipboard 🤣'


    @classmethod
    def get_instance(cls):
        """Returns a singleton instance of the Config class."""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
