
# `HtmlDoc` — PyFrontKit Documentation

## Overview

The `HtmlDoc` class is the **main entry point** for PyFrontKit. It allows you to create **complete HTML pages with CSS** programmatically using Python.

It handles:

* Generating the basic HTML structure (`<html>`, `<head>`, `<body>`).
* Applying global layout styles to the `body`.
* Adding JavaScript to the document.
* Writing the final files (`index.html` and `style.css`) to disk.

> ⚠️ Important: Always call `create_document()` **last**, after creating all blocks and adding content.
> Classes for styling (like `CreateFont`, `CreateColor`, etc.) are applied **after** `create_document()` because they work on the generated document, not in memory.

---

## Initialization

```python
from pyfrontkit import HtmlDoc

# Create a new HTML document
doc = HtmlDoc(
    title="My Page",
    path="./output",          # Directory where files will be created
    links=["reset.css"],      # Optional external stylesheets
    inline_style=None,        # Optional inline CSS for the <head>
    head_scripts=[]           # Optional scripts in <head>
)
```

**Parameters:**

| Parameter      | Type | Description                                        |
| -------------- | ---- | -------------------------------------------------- |
| `title`        | str  | The page title (`<title>`).                        |
| `path`         | str  | Directory to save the HTML and CSS files.          |
| `links`        | list | Optional list of CSS files to include in `<head>`. |
| `inline_style` | str  | Optional inline CSS added inside `<head>`.         |
| `head_scripts` | list | Optional list of JS files added inside `<head>`.   |

---

## Key Attributes

| Attribute       | Description                                        |
| --------------- | -------------------------------------------------- |
| `html_file`     | Full path to the generated HTML file.              |
| `css_file`      | Full path to the generated CSS file.               |
| `_body_scripts` | List of JavaScript snippets added with `script()`. |
| `links`         | Optional list of external CSS links.               |
| `inline_style`  | Optional inline CSS.                               |

---

## Main Methods

### `create_document()`

Generates the HTML and CSS files in the specified directory.

```python
doc.create_document()
# Generates index.html and style.css
```

* Registers all blocks (`Block`) and their styles.
* Adds any scripts defined with `script()`.
* Applies global `body` styles defined with `align()`.

> **Tip:** This should always be the last method you call. Any styling classes (`CreateFont`, `CreateColor`, etc.) should be applied after this.

---

### `align(orientation, gap=None, padding=None, grid_column=None)`

Applies layout styles to the `<body>` element.

```python
doc.align("column", gap="20px", padding="10px")
```

**Parameters:**

| Parameter     | Type | Description                                           |
| ------------- | ---- | ----------------------------------------------------- |
| `orientation` | str  | Layout type: `"column"`, `"row"`, or `"grid"`.        |
| `gap`         | str  | Spacing between child elements.                       |
| `padding`     | str  | Padding inside the `<body>`.                          |
| `grid_column` | int  | Number of columns (required if `orientation="grid"`). |

> **Example:** Use `align("row", gap="30px")` to create a horizontal layout for all top-level elements.

---

### `script(js_code)`

Adds a JavaScript snippet at the end of the `<body>`.

```python
doc.script("console.log('Hello from PyFrontKit');")
```

* Multiple scripts can be added.
* They execute in the order added.

> Example use: adding simple UI interactions, logging, or client-side behavior.

---

### `render_body()`

Generates HTML for all registered blocks with no parent.

* Usually **not called directly**.
* Automatically used inside `create_document()` to render the page body.

---

## Full Example

```python
from pyfrontkit import HtmlDoc, div, a

# 1️⃣ Create document
doc = HtmlDoc(title="My Page")

# 2️⃣ Apply body layout
doc.align("column", gap="30px", padding="20px")

# 3️⃣ Create top-level blocks
div(id="header", ctn_p="Welcome").align("row", gap="10px")
a(ctn_p="Login").hover("white", "#000")

# 4️⃣ Add JavaScript
doc.script("console.log('Hello from PyFrontKit');")

# 5️⃣ Generate final files
doc.create_document()
```

**Output:**

```
./output/index.html
./output/style.css
```

---

## Notes for Beginners

* `HtmlDoc` is **the first class you always instantiate**.
* Use `Block` or derived elements to add content.
* `create_document()` is the **final step**; nothing else should modify the document before this.
* Styling classes (like `CreateFont`, `CreateColor`, etc.) are applied **after** `create_document()`.

