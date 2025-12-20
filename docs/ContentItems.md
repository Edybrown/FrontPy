📝 ContentItem – PyFrontKit

ContentItem represents text content inside a Block. It allows you to add text with optional HTML tags, classes, and styles.

It is commonly used through Block with ctn_* kwargs (like ctn_p, ctn_span, ctn_h1).

⚡ Key Concepts

Text content with tags

ContentItem wraps text inside an HTML tag (<p>, <h1>, <span>, <b>, etc.).

If the tag is "none", it renders raw text without any tag.

New lines and <br />

Multi-line strings using triple quotes (""") automatically insert <br /> tags in the HTML.

Using \n in a string also generates <br /> automatically.

Optional class and style

You can add a CSS class and inline styles per content item.

✅ Supported Tags

Text tags: "p", "span", "b", "strong", "i", "u", "em", "small", "mark", "code"

Heading tags: "h1", "h2", "h3", "h4", "h5", "h6"

Raw text: "none"

🔹 Usage via ctn_*

Blocks accept kwargs starting with ctn_ followed by the tag name.

from pyfrontkit import Div

# Create a block with a paragraph
block = Div(
    ctn_p="Hello world!"
)

# With multi-line string using """ → generates <br />
block2 = Div(
    ctn_span="""Line one
Line two
Line three"""
)

# With tuple: (text, class, style)
block3 = Div(
    ctn_p=("Styled text", "highlight", "font-weight:bold;color:red;")
)


Explanation:

ctn_p="Hello" → creates <p>Hello</p>

Triple-quoted string → inserts <br /> automatically for line breaks

Tuple (text, class, style) → allows CSS class and inline styling

⚡ ContentFactory

ContentFactory is the helper class used internally to create ContentItem objects from ctn_* kwargs.

You usually do not need to call it directly; just pass ctn_* kwargs to any Block.

Example Full Block
from pyfrontkit import Div

block = Div(
    ctn_h1="Title here",
    ctn_p="""This is a paragraph
with multiple lines.""",
    ctn_span=("Important text", "highlight", "color:red;")
)


Generates HTML:

<h1>Title here</h1>
<p>This is a paragraph<br />with multiple lines.</p>
<span class="highlight" style="color:red;">Important text</span>