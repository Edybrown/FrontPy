🧱 Block Class – PyFrontKit

Block is the base class for container elements in PyFrontKit. It represents HTML elements that can contain other blocks, text, or media (like <div>, <section>, <article>, <header>, <footer>, etc.).

All specialized elements (like Div, Section, Header, Footer) inherit from Block.

Important: Users usually interact with Block through its subclasses, not directly.

⚡ Key Concepts

Children and content

Only blocks with an id can contain child blocks or text.

Textual content is passed via ctn_* arguments (like ctn_p="Hello").

Media blocks (video, audio, picture) follow HTML-specific rules.

Automatic registration

If no id or class is provided, PyFrontKit auto-generates an ID for the block.

Blocks with an id are globally registered for linking and style purposes.

🛠 Methods

Below are the user-facing methods for styling and layout. All sizes and dimensions are passed as strings (e.g., "100px", "50%", "10vh").

1️⃣ align()

Controls the layout of children inside this block.

block.align(orientation="row", gap="10px", padding="20px", text_align="center")


Parameters:

Parameter	Description
orientation	"row", "column", or "grid" – direction of child blocks.
gap	Space between children (e.g., "10px").
padding	Inner spacing inside the block (e.g., "20px").
pad_top	Padding top (overrides padding).
pad_right	Padding right (overrides padding).
pad_bottom	Padding bottom (overrides padding).
pad_left	Padding left (overrides padding).
grid_column	Number of columns if orientation="grid" (e.g., "3").
fsize	Font size (e.g., "16px").
text_align	"start", "left", "center", "end", "right", "expand"

Example:

Div(ctn_p="Hello World").align(orientation="column", gap="15px", text_align="center")

2️⃣ form()

Controls size, shape, and colors of the block.

block.form(width="200px", height="100px", border_radius="10px", background="#333", color="#FFF")


Parameters:

Parameter	Description
width	Block width ("200px", "50%", etc.).
height	Block height ("100px", "auto", etc.).
border_radius	Rounded corners ("10px", "50%").
background	Background color ("#FFF", "red", "rgb(255,0,0)").
color	Text color inside the block.

Example:

Div(ctn_p="Button").form(width="150px", height="50px", background="#3498db", color="white", border_radius="5px")

3️⃣ position()

Sets absolute positioning of the block.

block.position(top="20px", left="50px", z_index=10)


Parameters:

Parameter	Description
top	Distance from top of container ("20px").
left	Distance from left ("50px").
right	Distance from right.
bottom	Distance from bottom.
z_index	Stack order for overlapping blocks.
4️⃣ border()

Adds border styling.

block.border(size="2px", style="dashed", color="#000")


Parameters:

Parameter	Description
size	Border thickness (e.g., "2px").
style	"solid", "dashed", "dotted", "double", "groove", "ridge", "inset", "outset", "none", "hidden".
color	Border color ("#000", "red", etc.).
5️⃣ shadow()

Applies box shadow.

block.shadow(x="2px", y="4px", blur="6px", spread="0px", color="#888", inset=False)


Parameters:

Parameter	Description
x	Horizontal offset ("2px").
y	Vertical offset ("4px").
blur	Blur radius ("6px").
spread	Spread radius ("0px").
color	Shadow color.
inset	If True, creates inner shadow.
6️⃣ margin()

Sets external spacing around the block.

block.margin(top="10px", bottom="10px")


Parameters:

Parameter	Description
top	Margin top.
right	Margin right.
bottom	Margin bottom.
left	Margin left.
7️⃣ hover()

Adds hover effect for interactivity.

block.hover(color="white", background="#3498db", scale=1.05, transition="0.3s")


Parameters:

Parameter	Description
color	Text color on hover.
background	Background color on hover.
scale	Enlargement factor on hover (1.1 = 10% bigger).
transition	Duration of hover effect ("0.2s" by default).
✅ Usage Example
from pyfrontkit import HtmlDoc, Div, Section

doc = HtmlDoc("My Page", path="./output/")

header = Div(ctn_p="Welcome").form(width="100%", height="60px", background="#2c3e50", color="white")
header.align(orientation="row", gap="10px", padding="10px")
header.hover(background="#34495e", scale=1.05)

section = Section(ctn_p="Main Content").form(width="80%", height="400px", background="#ecf0f1")
section.align(orientation="column", gap="20px", text_align="center")

doc.create_document()


This will generate an HTML page with styled blocks that respect the layout, colors, and hover interactions.

Notes

All sizes, spacing, and colors are passed as strings ("px", "%", "vh").

Styling methods must be called before create_document() if they affect the block content.

create_document() finalizes the HTML and CSS files; style classes like CreateColor or CreateFont work after this.