# FletTest

Welcome to **FletTest**! 🎉 This repository was created as a playground to explore and test the [Flet framework](https://flet.dev/). It's a lightweight yet powerful project that showcases some of Flet's core features, including theming, Markdown rendering, and custom code blocks with copy functionality.

![Preview](https://raw.githubusercontent.com/timoinglin/FletTest/refs/heads/main/preview.jpg?token=GHSAT0AAAAAAC2IA6MRO5RZJHFR6FWWEUOUZZWNPYA)


## Features

### 🌗 Dark/Light Theme
Easily switch between dark and light themes, offering a visually pleasing experience for all users.

### 📄 Markdown Support
The app reads a Markdown (`.md`) file and dynamically displays its content on the page. Perfect for documentation or content-heavy pages.

### 🖥️ Custom Code Blocks
For any code snippets:
- **Stylish Code Blocks**: Includes its own design for displaying code snippets.
- **Copy Button**: Quickly copy code with a single click.
- **Customizable Colors**: The colors of the code block are fully customizable through the settings file.

### 📋 Collapsible Sidebar
The app includes a **collapsible sidebar** with smooth animations:
- **Expand/Collapse with Animation**: Toggle the sidebar to optimize screen space while maintaining easy navigation.
- **Customizable Width**: Adjust the sidebar width via the settings file to suit your preferences.

### ⚙️ App Settings
The app comes with a flexible `settings.ini` file where you can tweak various parameters to tailor the app to your needs. Here's a quick overview of the settings:

#### General Settings
- **Leftbar Width**: Customize the width of the sidebar.
- **Docs Page Title**: Set your documentation page's title.

#### Top Bar
- Adjust logo size, top bar height, menu alignment, and text size.
- Set the text for the documentation button.

#### Footer
- Fully customizable footer, supporting Markdown.
- Adjust alignment and height of the footer text.

#### Code Block Customization
- Define colors, tooltips, and notification messages for code blocks.
- Make your code blocks visually appealing and interactive.

### 📱 Responsive Layout
The app layout is fully responsive, ensuring it works seamlessly on devices of all sizes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/timoinglin/FletTest.git
   ```
2. Navigate to the project folder:
   ```bash
   cd FletTest
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python main.py
   ```

## Customization

Modify the `settings.ini` file to adjust the app's appearance and functionality according to your preferences. Here's a sample snippet of the settings file:

```ini
[general]
# leftbar_width: Specifies the width of the leftbar in pixels.
leftbar_width = 200

# docs_page_title: Sets the title for the documentation page
docs_page_title = FletTest 🚀 My cool app


[top_bar]
# logo_width: Specifies the width of the logo in pixels.
logo_width = 50

# top_bar_height: Specifies the height of the top_bar in pixels.
top_bar_height = 60

# menu_alignment: Determines the alignment of the menu.
# Options: 
# - left: Aligns the menu to the left.
# - center: Centers the menu.
# - end: Aligns the menu to the right.
menu_alignment = center

# top_bar_text_size: Specifies the font size in pixels of the text in the top bar.
top_bar_text_size = 16

# docs_button_text: Display text for the documentation menu buton.
docs_button_text = Docs


[footer]
# footer_text: Display text in the app footer. Supports Markdown.
# Example: Copyright © 2024 | [Your Company](https://yourcompany.com)
footer_text = 

# footer_alignment: Determines the alignment of the text in the footer.
# Options: 
# - left: Aligns the text to the left.
# - center: Centers the text.
# - end: Aligns the text to the right.
footer_alignment = center

# footer_height: Specifies the height of the footer in pixels.
footer_height = 60


[codeblock]
# codeblock_copy_tooltip: Text displayed as a tooltip for the copy button.
codeblock_copy_tooltip = Copy code

# codeblock_top_bgcolor: Background color of the codeblock's top bar, specified as a hex color code.
codeblock_top_bgcolor = "#272A2C"

# codeblock_copy_icon_color: Color of the copy button icon, specified as a hex color code.
codeblock_copy_icon_color = "#FFFFFF"

# codeblock_body_bgcolor: Background color of the codeblock's main content area, specified as a hex color code.
codeblock_body_bgcolor = "#0E1114"

# codeblock_text_color: Color of the text within the codeblock, specified as a hex color code.
codeblock_text_color = "#FFFFFF"

# codeblock_border_color: Color of the codeblock's border, specified as a hex color code.
codeblock_border_color = "#222222"

# copied_alert_text: Text displayed for notification when code is copied
copied_notification_text = Code snatched! Now chilling on your clipboard 🤣
```

## Roadmap

This project was designed for testing and learning purposes, but feel free to fork or expand it with new features, such as:
- Enhanced Markdown support.
- More customization options.
- Additional themes or layouts.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Enjoy exploring the Flet framework, and happy coding! 😊