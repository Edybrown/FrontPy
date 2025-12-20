
# 🖋️ Typography & Font System

PyFrontKit provides a dual-layer approach to typography. You can define a **global design system** using font classes while maintaining the flexibility to override specific elements using **Block methods**.

## 📌 The Hierarchy of Text Control

The library manages text through a complementary relationship between two systems:

1. **Structural Classes (`CreateFont`, `MainFont`, `FooterFont`)**: These set the "baseline" styles for specific zones (Global, Main, or Footer) and target the most common text tags: `h1`, `h2`, `h3`, and `p`.
2. **Granular Methods (`.align()`)**: The `Block.align()` method allows you to fine-tune specific instances using `fsize` (font-size) and `text_align`.

---

## 🚀 Global & Zonal Styling

### 1. `CreateFont` (Global Style)

This is the root of your typography. It applies the font family and default color to the `<body>`, which then trickles down to the rest of the document.

```python
from pyfrontkit import CreateFont

# Set global typography
CreateFont(family="Ebrima", color="#333", p="16px", h1="40px")

```

### 2. Zonal Classes ('HeaderFont,`MainFont` & `FooterFont`)

These classes are "children" of the font system designed to help you style specific regions without writing complex CSS selectors.

* **`MainFont`**: Targets text specifically inside the `<main>` tag.
* **`FooterFont`**: Targets text specifically inside the `<footer>` tag.
* **'FooterFont'**: Targets text specifically inside the `<header>` tag
```python
from pyfrontkit import FooterFont

# Footer text is usually smaller and more subtle
FooterFont(family="Arial", color="grey", p="12px")

```

---

## 🛠️ The Complementary System: `Block.align()`

While the font classes handle the general rules for `h1-h3` and `p`, you will often need to break those rules for specific layouts (like a hero section or a specialized button).

In these cases, the **`align()`** method acts as a complement:

* **`fsize`**: Overrides the font size defined in your global or zonal font class.
* **`text_align`**: Controls the horizontal position (left, center, right) for that specific block.

### Integration Example:

```python
# 1. Set the general rule
CreateFont(family="Ebrima", p="16px")

# 2. Override for a specific high-impact block
div(id="hero_text").align(text_align="center", fsize="60px")

# 3. Use after this method create_document()
```

---

## 📋 Technical Constraints

* **Tag Limitation**: The font system classes specifically target `p`, `h1`, `h2`, and `h3`. For other tags (like `strong` or `span`), use the `.form()` or `.align()` methods directly on the block.
* **Safety**: 'HeaderFont' ,`FooterFont` and `MainFont` include safety checks; they will raise a `TypeError` if you call them without at least one styling argument, ensuring your CSS remains clean and functional.

