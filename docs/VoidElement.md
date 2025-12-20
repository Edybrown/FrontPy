⚡ VoidElement Class – PyFrontKit

VoidElement is the base class for self-closing HTML elements that cannot contain child elements. Examples include <img>, <input>, <hr>, <link>, <source>, and others.

Void elements are used for content that does not wrap other elements, like images, horizontal lines, external resources, or input fields.

All specific void elements inherit from VoidElement.

🛠 Key Concepts

Self-closing

Void elements automatically generate a self-closing HTML tag: <tag ... />.

They cannot contain children. Attempting to add a child will raise an error.

Attributes

Each void element has a list of allowed attributes (like src for <img> or href for <link>).

Attributes like id, class, style, title are always allowed.

Boolean attributes (checked, disabled, readonly) can be set with True.

All other values are passed as strings (e.g., "200px", "#fff", "text").

🏷 Concrete Void Elements
1️⃣ Img

Represents <img> for images.

img(src="photo.jpg", alt="A beautiful scene", width="200px", height="150px")


Common attributes: src, alt, width, height, loading, srcset, sizes.

Use it whenever you need to display an image on the page.

2️⃣ Input

Represents <input> fields in forms.

Input_(type="text", name="username", placeholder="Enter your name", value="")


Common attributes: type, name, value, placeholder, checked, disabled, readonly, min, max, step.

Use it for text fields, checkboxes, radio buttons, number inputs, and more.

3️⃣ Hr

Represents <hr> for horizontal lines.

hr(style="border: 1px solid #ccc;")


Use it to visually separate content sections.

4️⃣ Link

Represents <link> for external resources like CSS.

link(href="style.css", rel="stylesheet")


Common attributes: href, rel, type, media, crossorigin.

Use it to include stylesheets or preload resources.

5️⃣ Source

Represents <source> inside <video> or <audio> elements.

source(src="video.mp4", type="video/mp4")


Attributes: src, type, srcset.

Use it to define multiple media sources for adaptive playback.

6️⃣ Embed

Represents <embed> to include external content like PDFs or plugins.

embed(src="document.pdf", type="application/pdf", width="600px", height="400px")

7️⃣ Param

Represents <param> used inside <object> tags to pass parameters.

param(name="autoplay", value="true")

8️⃣ Track

Represents <track> for subtitles/captions in <video>.

track(kind="subtitles", src="subtitles.vtt", srclang="en", label="English")

9️⃣ Wbr

Represents <wbr> for optional word breaks.

wbr()

10️⃣ Other Void Elements
Element	Purpose
Area	Defines clickable regions in image maps (<map>).
Base	Sets the base URL for relative links.
Col	Defines column properties in <table> elements.
✅ Usage Notes

Instantiation: Use the lowercase aliases for simpler syntax: img(...), hr(), Input_(...).

Self-closing: Void elements automatically close themselves; no children allowed.

Attributes: All sizes, URLs, and colors must be passed as strings ("200px", "50%", "#FFF").

Registration: All void elements are registered in the global Block._registry, so they participate in global layout if needed.

Example
from pyfrontkit import HtmlDoc, Div, img, hr, Input_

doc = HtmlDoc("Void Example", path="./output/")

header = Div(ctn_p="Welcome")
header.form(width="100%", height="60px", background="#2c3e50", color="white")

# Add image
header_image = img(src="logo.png", alt="Logo", width="100px", height="50px")
header.add_child(header_image)

# Add input field
user_input = Input_(type="text", name="username", placeholder="Enter your name")
header.add_child(user_input)

# Add horizontal line
header.add_child(hr())

doc.create_document()


This generates HTML with images, input fields, and a horizontal line, all correctly formatted as self-closing elements.