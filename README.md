# FletTest

Welcome to **FletTest**! 🎉 This repository was created as a playground to explore and test the [Flet framework](https://flet.dev/). It's a lightweight yet powerful project that showcases some of Flet's core features, including theming, Markdown rendering, and custom code blocks with copy functionality.

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
   git clone https://github.com/your-username/FletTest.git
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
leftbar_width = 200
docs_page_title = FlashDoc 🚀 Empowering Documentation

[top_bar]
logo_width = 50
menu_alignment = center

[footer]
footer_text = Copyright © 2024 | [Your Company](https://yourcompany.com)
footer_alignment = center

[codeblock]
codeblock_copy_tooltip = Copy code
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