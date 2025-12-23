
---

# `HtmlDoc` — PyFrontKit Documentation

## Overview

The `HtmlDoc` class is the **main entry point** for PyFrontKit.
It allows you to **define, assemble, and render complete HTML documents with CSS** using pure Python.

`HtmlDoc` supports **two rendering modes**:

1. **File-based rendering** — generate physical HTML and CSS files on disk.
2. **In-memory rendering** — generate HTML (and CSS) as Python strings.

It handles:

* Generating the base HTML structure (`<html>`, `<head>`, `<body>`).
* Managing a document-local internal DOM during creation.
* Applying global layout styles to the `<body>`.
* Collecting and rendering JavaScript snippets.
* Rendering output **to disk or directly in memory**, depending on the workflow.

> ⚠️ Important
> `HtmlDoc` does **not** expose or persist a global DOM.
> Each render builds a **local, temporary document model** that is discarded after output is generated.

---

## Initialization

```python
from pyfrontkit import HtmlDoc

doc = HtmlDoc(
    title="My Page",
    path="./output",          # Directory where files will be created (file-based rendering)
    links=["reset.css"],      # Optional external stylesheets
    inline_style=None,        # Optional inline CSS for the <head>
    head_scripts=[]           # Optional scripts in <head>
)
```

### Parameters

| Parameter      | Type | Description                                           |
| -------------- | ---- | ----------------------------------------------------- |
| `title`        | str  | The page title (`<title>`).                           |
| `path`         | str  | Directory used by `create_document()` to write files. |
| `links`        | list | Optional list of CSS files included in `<head>`.      |
| `inline_style` | str  | Optional inline CSS added to `<head>`.                |
| `head_scripts` | list | Optional external scripts added to `<head>`.          |

---

## Key Attributes

| Attribute       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `html_file`     | Full path to the generated HTML file (file-based rendering). |
| `css_file`      | Full path to the generated CSS file (file-based rendering).  |
| `_body_scripts` | List of JavaScript snippets added via `script()`.            |
| `links`         | External stylesheet links included in `<head>`.              |
| `inline_style`  | Optional inline CSS for `<head>`.                            |

---

## Rendering Modes

`HtmlDoc` supports two distinct rendering workflows.

### 1️⃣ File-Based Rendering (`create_document()`)

This mode generates physical files on disk and is intended for:

* Static site generation
* Build-time workflows
* Exporting HTML/CSS for manual editing

#### `create_document()`

```python
doc.create_document()
```

This method:

* Registers all created blocks and their styles.
* Generates `index.html` and `style.css`.
* Applies global body layout styles (`align()`).
* Writes files to the directory defined by `path`.

> **Important**
> `create_document()` should be the **final step** of the document creation process.
> Styling systems such as `CreateFont` or `CreateColor` are applied **after** this call because they operate on generated files.

---

### 2️⃣ In-Memory Rendering (`create_template()`)

This mode renders the document **entirely in memory**, without creating files on disk.

It is designed for:

* Template reuse
* Dynamic serving
* Testing
* Integration with servers or external frameworks

#### `create_template(css=True, inline=True)`

```python
html = doc.create_template()
```

##### Parameters

| Parameter | Type | Description                                                                                      |
| --------- | ---- | ------------------------------------------------------------------------------------------------ |
| `css`     | bool | Enables or disables CSS generation.                                                              |
| `inline`  | bool | If `True`, CSS is embedded in a `<style>` tag. If `False`, HTML and CSS are returned separately. |

##### Return Values

```python
# Inline CSS (single string)
html = doc.create_template()

# Separate HTML and CSS
html, css = doc.create_template(inline=False)
```

---

## Stateless Rendering Model

After `create_template()` is executed, **all internal registries are cleared**.

This guarantees:

* No shared state between renders
* Safe reuse across multiple calls
* Independent output for each execution
* Compatibility with concurrent or iterative workflows

Each call to `create_template()` produces a **fully independent document**.

---

## Body Layout

### `align(orientation, gap=None, padding=None, grid_column=None)`

Applies layout styles directly to the `<body>` element.

```python
doc.align("column", gap="20px", padding="10px")
```

| Parameter     | Type | Description                       |
| ------------- | ---- | --------------------------------- |
| `orientation` | str  | `"column"`, `"row"`, or `"grid"`. |
| `gap`         | str  | Space between child elements.     |
| `padding`     | str  | Inner padding of the `<body>`.    |
| `grid_column` | int  | Required when using grid layout.  |

---

## JavaScript Injection

### `script(js_code)`

Adds raw JavaScript at the end of the `<body>`.

```python
doc.script("console.log('Hello from PyFrontKit');")
```

Scripts are rendered **in order of insertion**.

---

## Internal Rendering

### `render_body()`

Renders all top-level blocks (blocks without a parent).

* Automatically used by both rendering modes.
* Typically not called directly.

---

## Full Example (File-Based)

```python
from pyfrontkit import HtmlDoc, div, a

doc = HtmlDoc(title="My Page")

doc.align("column", gap="30px", padding="20px")

div(id="header", ctn_p="Welcome").align("row", gap="10px")
a(ctn_p="Login").hover("white", "#000")

doc.script("console.log('Hello from PyFrontKit');")

doc.create_document()
```

**Output:**

```
./output/index.html
./output/style.css
```

---

## Notes

* `HtmlDoc` manages document creation and rendering only.
* It does not enforce application logic or routing.
* Templates are typically defined as **Python functions** that return `create_template()` output.
* For template composition patterns, see `docs/templates.md`.

---

