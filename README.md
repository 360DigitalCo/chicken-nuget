# 🐔 Chicken NuGet

> **Build HTML with Python. No templates. No regrets.**

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-amber)](https://python.org)
[![Zero dependencies](https://img.shields.io/badge/dependencies-zero-green)](.)
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

---

```
╭─╴╷ ╷╷╭─╴╷╭ ╭─╴╭╮╷   ╭╮╷╷ ╷╭─╴╭─╴╶┬╴
│  ├─┤││  ├┴╮├╴ │╰┤   │╰┤│ ││╶╮├╴  │ 
╰─╴╵ ╵╵╰─╴╵ ╵╰─╴╵ ╵   ╵ ╵╰─╯╰─╯╰─╴ ╵ 
```

Every HTML tag is a Python object. Nest them. Chain them. Pass them to functions. Print them.

**[▶ Try it in the browser](https://360digital.github.io/chicken-nuget)**

---

## Installation

```bash
pip install chicken-nuget
```

## Quick start

```python
from chicken import html, head, body, div, p, h1, a, meta, title
from chicken import render_page, style

page = html(
    head(
        meta(charset="utf-8"),
        title("My Page"),
    ),
    body(
        div(class_="container",
            h1("Hello from Chicken NuGet 🐔"),
            p("Build HTML without leaving Python."),
            a("GitHub", href="https://github.com/360Digital/chicken-nuget"),
            style=style(max_width="640px", margin="2rem auto",
                        font_family="Courier New, monospace"),
        )
    )
)

print(render_page(page))
# → <!DOCTYPE html>
# → <html>
# →   <head>...
```

---

## API

### Tags

Every HTML tag is a callable that accepts `*children` and `**attrs`:

```python
div("hello")                         # <div>hello</div>
div(p("hi"), p("there"))             # nested children
a("click", href="#", class_="btn")   # attrs as kwargs
input_(type="text", disabled=True)   # boolean attrs
img(src="cat.png", alt="a cat")      # void elements (no closing tag)
```

**Keyword name rules:**
- Trailing `_` stripped: `class_` → `class`, `for_` → `for`
- Internal `_` → `-`: `data_value` → `data-value`

### Fluent methods

```python
div().add(p("a"), p("b"))            # append children, returns self
div().attr(id="box", class_="main")  # set attrs, returns self
```

### `style(**props)` → `str`

Converts Python kwargs to an inline CSS string:

```python
style(color="red", font_size="16px", margin_top="1rem")
# → "color: red; font-size: 16px; margin-top: 1rem;"
```

Underscores become hyphens. Pass the result to `style=`:

```python
div("hello", style=style(background="#fffbe6", padding="1rem"))
```

### `render(element, doctype=False, minify=False)` → `str`

```python
render(p("hi"))                        # "<p>hi</p>"
render(html(...), doctype=True)        # "<!DOCTYPE html>\n<html>..."
render(page, minify=True)              # single-line output
```

### `render_page(element)` → `str`

Shorthand for `render(element, doctype=True)`.

### `to_file(element, path, doctype=True, minify=False)`

```python
to_file(page, "index.html")
```

### `Raw(*children)`

Inject raw HTML strings without any wrapper element:

```python
Raw("<!-- Google Analytics -->", "<script>...</script>")
```

---

## Component pattern

```python
from chicken import div, h2, p, a, render

def card(title, body, href=None):
    children = [h2(title), p(body)]
    if href:
        children.append(a("Read more →", href=href))
    return div(*children, class_="card")

grid = div(
    card("Zero deps",   "Pure Python.",  "#"),
    card("Composable",  "Just objects.", "#"),
    class_="grid"
)

print(render(grid, doctype=True))
```

---

## Examples

```bash
python examples/basic.py > output.html
python examples/page_builder.py > output.html
```

---

## Development

```bash
git clone https://github.com/360Digital/chicken-nuget
cd chicken-nuget
pip install -e ".[dev]"
pytest
```

---

## Why "Chicken NuGet"?

Because `.nuget` is a package manager, chicken is delicious, and sometimes you just need to name something before you build it.

---

Made with ❤️ and Courier New by **[360Digital, Co.](https://github.com/360DigitalCo)**
