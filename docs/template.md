# Templates — PyFrontKit Documentation

## Overview

In PyFrontKit, **templates are plain Python functions**.

There is no separate template language, no hidden context, and no runtime engine.
A template is simply a function that:

1. Builds a document using PyFrontKit blocks
2. Calls `create_template()`
3. Returns the rendered output

This approach keeps templates:

* reusable
* testable
* composable
* fully integrated with Python logic

---

## Why Templates Are Functions

PyFrontKit intentionally avoids string-based templates or custom DSL syntax.

Using Python functions allows you to:

* Use native control flow (`if`, `for`, `match`)
* Reuse logic naturally
* Share templates across modules
* Call templates from any part of your application

> A PyFrontKit template is just Python code that returns HTML (and CSS).

---

## Basic Template Example

```python
from pyfrontkit import HtmlDoc, Div

def simple_template(message):
    doc = HtmlDoc(title="Simple Page")
    Div(ctn_p=message)
    return doc.create_template()
```

Usage:

```python
html = simple_template("Hello from PyFrontKit")
```

The result is a fully rendered HTML document generated in memory.

---

## Templates With Separate CSS

You can choose to return HTML and CSS separately.

```python
def page_template(title, text):
    doc = HtmlDoc(title=title)
    Div(ctn_p=text)
    return doc.create_template(inline=False)
```

Usage:

```python
html, css = page_template("Home", "Welcome")
```

This gives you **full control** over how and where the CSS is served.

---

## Reusing Templates Across Files

Templates can live in any Python module.

```python
# templates/login.py
def login_template(user):
    doc = HtmlDoc(title="Login")
    Div(ctn_p=f"Welcome {user}")
    return doc.create_template()
```

```python
# app.py
from templates.login import login_template

html = login_template("Pedro")
```

No special loader.
No configuration.
Just Python imports.

---

## Templates and Business Logic

Because templates are functions, they integrate naturally with application logic.

```python
def user_page(user):
    if user.is_admin:
        return admin_template(user)
    return regular_template(user)
```

This keeps:

* rendering logic separate
* decision-making explicit
* templates easy to reason about

---

## Multiple Renders and Statelessness

Each call to `create_template()`:

* builds a local document
* renders HTML and CSS
* clears all internal registries

This means you can safely do:

```python
for user in users:
    html = user_page(user)
```

Every iteration produces a **clean, independent document**.

---

## Integration Examples

PyFrontKit does not depend on any framework.
Templates can be integrated anywhere HTML is required.

### Example: HTTP Server (conceptual)

```python
html = page_template("Home", "Welcome")
connection.send(html.encode())
```

---

### Example: Flask / FastAPI (conceptual)

```python
@app.get("/")
def index():
    html = home_template()
    return HTMLResponse(html)
```

No adapters or plugins are required.

---

## When to Use Templates

Templates are ideal when you need:

* dynamic HTML generation
* reusable page layouts
* server-side rendering
* testable document output
* Python-driven frontend workflows

---

## What Templates Are Not

Templates in PyFrontKit are **not**:

* string replacements
* magic contexts
* runtime engines
* tied to a specific framework

They are explicit, readable, and predictable Python code.

---

## Summary

* Templates are plain Python functions
* Rendering is explicit via `create_template()`
* Output can be inline or separated
* No global state is shared
* Integration is framework-agnostic

PyFrontKit templates follow Python’s philosophy:
**simple, explicit, and powerful**.

---

## Related Documentation

* `docs/htmldoc.md` — document creation and rendering
* `docs/integration.md` — framework integration examples (optional)
* `docs/styling.md` — styling systems and CSS generation

