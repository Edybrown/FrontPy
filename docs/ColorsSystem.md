This is the official documentation for the PyFrontKit color management system. This guide will help you understand how to automate your website's aesthetic using intelligent color harmonies and distribution templates.
🎨 Color Management in PyFrontKit

PyFrontKit provides a sophisticated engine to apply cohesive color schemes across your entire project with a single command. It bridges the gap between raw CSS and design theory by using Families (harmonies) and Templates (distribution rules).
📌 Core Concepts

    Templates: These act as a "map" that dictates which HTML elements receive specific roles (e.g., which tags become the background color versus the text color).

    Color Families: Based on classic color theory, these ensure that the colors chosen for your site are visually harmonious.

    Dynamic Adjustment: For complex families like triadic or tetradic, the library automatically adjusts Lightness (L) and Saturation (S) using HSL logic to ensure web usability and readability.

🚀 Class CreateColor

Use this class when you want the library to generate a professional palette for you based on a single base color.
Usage
Python

from pyfrontkit    CreateColor

# Generates a Triadic harmony based on "blue_pure" using the "Standard" template
CreateColor(color_name="blue_pure", family="triadic", template="standard_light")

Parameters

    color_name: The specific key from the palettes (e.g., "red_pure", "sky_blue", "lime", "gold").

    family: The harmony logic to use:

        monochromatic: Different shades of the same hue.

        homologous / homologous_v2: Colors that are adjacent or related on the wheel.

        triadic: Three colors equally spaced around the color wheel.

        tetradic: Four colors arranged into two complementary pairs.

    template: The rule set for color distribution.

🛠️ Class CreateWithColor

Use this class if you already have a specific brand palette (HEX codes) and want to apply it using PyFrontKit's templates.
Usage
Python

from pyfrontkit import CreateWithColor

CreateWithColor(
    primary="#A5E12D", 
    secondary="#2F2F32", 
    tertiary="#FFFFFF", 
    template="professional_dark"
)

Parameters

    primary, secondary, tertiary: Required HEX strings.

    quaternary: Optional HEX string for extra detail.

    template: The distribution rule.

📋 Available Templates & Families

To use these classes, you must use the exact names defined in the library.
1. Color Families (family)

These are the available harmony logics found in palettes.py:

    monochromatic

    triadic

    tetradic

    homologous

    homologous_v2

2. Style Templates (template)

Templates determine how colors are assigned to tags like body, header, a, or p. Common names found in colors_templates.py include:

    simple
    classic
    dark_reverse
    mono
    enfasis_main
    soft
    classic_reverse
    asimetric
    total
    darkness
    mono_accent
    total_v2
💡 Pro-Tips

    CSS Injection: When you call these classes, PyFrontKit automatically scans your style.css and injects the colors into the matching selectors.

    Override with .form(): Styles applied via CreateColor are global. You can always override a specific element's color by using the .form(color="...") method on a Block object for more granular control.

    Void Tags: Elements like <img> or <hr> are handled separately within the templates to ensure borders or backgrounds match the theme.