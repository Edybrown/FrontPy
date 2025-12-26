# Framework Integration — PyFrontKit

PyFrontKit does not replace your web framework.
It integrates with them naturally by treating HTML rendering as plain Python code.

Because PyFrontKit templates are **Python functions that return HTML (and CSS)**,
they can be used unchanged across different frameworks.

---

## Core Idea

A PyFrontKit template:

- is a Python function
- receives data as arguments
- returns rendered HTML (and optionally CSS)

This makes templates:

- framework-agnostic
- easy to test
- easy to reuse
- easy to compose

There are no adapters, loaders, or plugins involved.

---

## Django Integration

In Django, PyFrontKit templates can be used inside standard views.

```python
# views.py
from django.http import HttpResponse
from templates.home import home_template

def home(request):
    html = home_template(user=request.user)
    return HttpResponse(html)

Nothing special is required:

    no template engine

    no context processors

    no template directories

PyFrontKit works as a pure rendering step.
Flask Integration

In Flask, templates can be returned directly from route handlers.

from flask import Flask, Response
from templates.home import home_template

app = Flask(__name__)

@app.route("/")
def home():
    html = home_template(user="Pedro")
    return Response(html, mimetype="text/html")

No configuration is needed.
The template function is imported and called like any other Python function.
FastAPI Integration

FastAPI works naturally with PyFrontKit due to its Python-first design.

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from templates.home import home_template

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html = home_template(user="Pedro")
    return html

Templates remain synchronous, explicit, and predictable.
Returning Separate HTML and CSS

If a template returns HTML and CSS separately:

html, css = page_template("Home", "Welcome")

You are free to:

    inline CSS

    serve it as a static file

    cache it

    inject it into a response pipeline

Frameworks remain fully in control.
Dynamic Layouts and Themes

Because templates are functions, layout decisions can be made dynamically.

def page(user):
    if user.is_admin:
        return admin_layout(user)
    return default_layout(user)

No template inheritance.
No magic overrides.
Just Python logic.
When PyFrontKit Fits Best

PyFrontKit integrates well when you want:

    server-side HTML generation

    reusable layouts as code

    dynamic UI decisions

    testable rendering output

    one rendering model across multiple frameworks

What PyFrontKit Does Not Do

PyFrontKit does not:

    manage routing

    replace your framework

    impose a project structure

    introduce a runtime template engine

It focuses only on explicit HTML and CSS generation.
Summary

    Templates are Python functions

    Integration requires no adapters

    The same template works across frameworks

    Rendering stays explicit and predictable

PyFrontKit fits where Python logic and UI generation meet.
