# PyFrontKit  
### A Python DSL for Programmatic HTML & CSS Generation

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

**PyFrontKit** is a Python library that lets you **generate clean, production-ready HTML and CSS using pure Python**, without replacing web standards and without hiding them.

It is not a framework.  
It is a **tool for structure, control, and clarity**.

---

## 🌍 What PyFrontKit Is (and Is Not)

### ✔ What it **is**
- A **Pythonic DSL** to generate HTML and CSS
- A tool to reduce boilerplate while keeping full control
- A system that produces **real, editable HTML and CSS**
- Designed for developers who already understand what they want to build
- Suitable for **production use**

### ✖ What it is **not**
- It does **not replace HTML, CSS, or JavaScript**
- It does **not hide the DOM**
- It does **not generate layouts automatically**
- It is **not a visual builder**

PyFrontKit helps you **write less**, not **think less**.

---

## 🧠 Philosophy

PyFrontKit follows a simple principle:

> **Structure first. Automation second. Control always.**

You describe your document structure using Python.
PyFrontKit generates clean output files:

```

index.html
style.css

````

No runtime. No browser dependency. No abstraction leaks.

---

## 🧩 How Structure Works

### Blocks, IDs, and Content

- **Blocks** represent HTML elements (`div`, `section`, `header`, etc.)
- **`ctn_` parameters** define textual content inside a block
- **`id` is optional** and should be used **only when a block needs to receive children later**

### Important rule

> **`ctn_` content is NOT a child block.  
> Only blocks passed as arguments become children.**

This means:

```python
Footer(ctn_p="© 2025 PyFrontKit")
````

✔ Valid
✔ No `id` required
✔ No children expected

But if you want to add content later:

```python
Footer(id="page_footer")
page_footer(
    Div(ctn_p="© 2025 PyFrontKit")
)
```

✔ `id` is required
✔ The block can now receive children

---

### ⚠️ ID Naming Recommendation

Do **not** use tag names as IDs.

❌ Bad:

```python
Footer(id="footer")
```

✅ Good:

```python
Footer(id="page_footer")
```

IDs represent **meaning**, not structure.

---

## ✍️ Content System (`ctn_`)

Text is written naturally using Python strings:

```python
Div(
    ctn_p="""This is line one
This is line two"""
)
```

* Line breaks (`\n`) automatically generate `<br />`
* Triple-quoted strings are fully supported
* Supported tags include:

  * `p`, `span`
  * `h1`–`h6`
  * `strong`, `em`, `code`, `mark`, etc.

This system is handled internally by **ContentItems**.

---

## 🎨 Styling Overview

Styling is **never forced**.

You can mix and choose:

### 1️⃣ Inline styles (fast prototyping)

```python
Div(ctn_p="Hello", style="color:red; padding:10px;")
```

### 2️⃣ External CSS (recommended)

PyFrontKit automatically generates selectors in `style.css`:

```css
#page_footer {}
section {}
div {}
```

You edit them freely.

---

## 🎨 Color System (Optional)

PyFrontKit includes an optional **Color System**:

* `CreateColor`
* `CreateWithColor`

These classes:

* Apply predefined color palettes
* Distribute colors using named templates
* Work **after** `create_document()`

Available templates include:

```
simple, classic, soft, darkness,
mono, mono_accent,
total, total_v2,
classic_reverse, dark_reverse, asimetric, enfasis_main
```

### Two approaches

#### ✔ `CreateColor`

Uses predefined palettes and families.

#### ✔ `CreateWithColor`

Lets you define your own colors manually and still use templates.

You can always refine or override colors using:

* CSS
* `Block.form()` methods

---

## ✒️ Typography System (Optional)

Typography helpers allow you to:

* Load external fonts (Google Fonts or custom)
* Separate body, header, and footer typography
* Apply styles at CSS level

Typography is never hardcoded.

---

## 📄 Basic Example

```python
from pyfrontkit import HtmlDoc, Header, Section, Div, Footer

doc = HtmlDoc(title="PyFrontKit Example")

Header(ctn_h1="Welcome to PyFrontKit")

Section(id="content")
content(
    Div(ctn_p="This page was generated entirely with Python.")
)

Footer(ctn_p="© 2025 PyFrontKit")

doc.create_document()
```

Output:

```
index.html
style.css
```

---

## 🧱 Main Systems

Documentation is split by responsibility:

* **HtmlDoc** – document creation and file output
* **Block** – structure and layout
* **ContentItems** – textual content (`ctn_`)
* **VoidElement** – self-closing tags (`img`, `hr`, `input`, etc.)
* **ColorSystem** – palettes and templates
* **TypographySystem** – fonts and text styling

📘 See `/docs` for full documentation.

---

## 🧪 Production Ready

* Tested with `pytest`
* Deterministic output
* No runtime execution
* Ideal for automation and CI pipelines

---

## 📦 Installation

```bash
pip install pyfrontkit
```

or

```bash
pip install git+https://github.com/Edybrown/pyfrontkit.git
```

---

## 🚀 Use Cases

* Static websites
* Documentation generators
* Landing pages
* UI prototyping
* Teaching HTML & CSS structure
* Python-driven frontend workflows

---

## 📄 License

GNU GPL v3
Free to use, modify, and redistribute under the same license.

---

## 👤 Author

Created by **Eduardo Antonio Ferrera Rodríguez**

A project focused on:

* Python DSL design
* Frontend structure
* Automation without abstraction loss
* Professional, maintainable output
