
# PyFrontKit

### A Python DSL for Building Web Views as Executable Code

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**PyFrontKit** is a Python library that lets you **build web views using pure Python**, producing clean, professional HTML and CSS without replacing or hiding web standards.

It is **not a framework** — it’s a **backend-friendly engine for structure, control, and clarity**.


## 🌟 Why PyFrontKit Exists

Developers often spend hours writing repetitive HTML and CSS. PyFrontKit allows you to:

* **Reduce boilerplate** while keeping full control
* Generate **real, editable HTML and CSS**
* Use Python logic (`if/else`, `for`) to shape your page dynamically
* Build production-ready pages **to disk** or **directly in memory**, with optional inline CSS

> **Structure first. Automation second. Control always.**

---

## 💡 What PyFrontKit Is (and Isn’t)

### ✔ It **is**:

* A Pythonic DSL for HTML and CSS
* A productivity tool that simplifies repetitive tasks
* A system that produces professional, **editable** code
* Suitable for **static sites, landing pages, and Python-driven frontends**

### ✖ It **is not**:

* A visual builder
* A framework that hides HTML/CSS
* A layout generator
* A runtime-dependent system

PyFrontKit helps you **write less without thinking less**.

---

## 🧱 Core Concepts

### Blocks and Content

* **Blocks** = HTML elements (`div`, `section`, `header`, etc.)
* **`ctn_` parameters** = textual content inside a block
* **IDs** are optional; required only for blocks receiving children later

```python
Footer(ctn_p="© 2025 PyFrontKit")  # simple block
Footer(id="page_footer")           # can receive children later
```

### Text Handling (`ContentItems`)

* Automatically converts line breaks (`\n`) into `<br />`
* Supports multiple tags (`p`, `span`, `h1`–`h6`, `strong`, `em`, `code`, `mark`)
* Full triple-quoted strings supported

---

## 🎨 Styling

### 1️⃣ Inline Styles (Fast Prototyping)

```python
Div(ctn_p="Hello", style="color:red; padding:10px;")
```

### 2️⃣ External CSS (Recommended)

PyFrontKit generates selectors in `style.css` that are **editable**:

```css
#page_footer {}
section {}
div {}
```

---

## 🎨 Color System (Optional)

* `CreateColor` → predefined palettes and templates
* `CreateWithColor` → define custom colors while using templates

Available templates:
`simple, classic, soft, darkness, mono, mono_accent, total, total_v2, classic_reverse, dark_reverse, asimetric, enfasis_main`

---

## ✒️ Typography System (Optional)

* Load custom or Google fonts
* Separate body, header, and footer typography
* Apply styles via CSS, never hardcoded

---

## 💻 Disk vs Memory

### Disk Mode

Generates files:

```
index.html
style.css
```

### Memory Mode

Returns a fully-rendered string, ready for frameworks like **FastAPI** or **Flask**, optionally with **inline CSS** for single-response delivery.

```python
doc.create_template()  # returns HTML+CSS string
```

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

doc.create_document()  # writes index.html + style.css
```

---

## 🖼️ Examples

PyFrontKit ships with **two professional examples**:

| File           | Description                                                 |
| -------------- | ----------------------------------------------------------- |
| `example_1.py` | Landing page with hero sections and grids                   |
| `example_2.py` | Multi-section page demonstrating color & typography systems |

> Check the `examples/` folder to see PyFrontKit in action.

---

## 🚀 Use Cases

* Static websites
* Documentation generators
* Landing pages
* UI prototyping
* Teaching HTML & CSS structure
* Python-driven frontend workflows

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

## 🧪 Production Ready

* Deterministic output
* Tested with `pytest`
* No runtime dependencies
* Ideal for automation & CI pipelines

---

## 👤 Author

**Eduardo Antonio Ferrera Rodríguez**
Focus: Python DSL, frontend structure, automation without abstraction loss, professional output

Licensed under **MIT License**
