"""
chicken.render
~~~~~~~~~~~~~~
Top-level rendering helpers.
"""

from __future__ import annotations
from .elements import Element

DOCTYPE = "<!DOCTYPE html>"


def render(element: Element, doctype: bool = False, minify: bool = False) -> str:
    """
    Render an element tree to an HTML string.

    Args:
        element:  Root element to render.
        doctype:  Prepend <!DOCTYPE html> (useful for <html> roots).
        minify:   Strip indentation and newlines for compact output.

    Returns:
        HTML string.
    """
    out = element.render()
    if minify:
        out = " ".join(out.split())
    if doctype:
        out = DOCTYPE + "\n" + out
    return out


def render_page(element: Element) -> str:
    """Shorthand: renders with DOCTYPE prepended."""
    return render(element, doctype=True)


def to_file(element: Element, path: str, doctype: bool = True, minify: bool = False) -> None:
    """Write rendered HTML to a file."""
    html = render(element, doctype=doctype, minify=minify)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def style(**props) -> str:
    """
    Convert a dict of CSS properties to an inline style string.

    Example:
        style(color="red", font_size="16px")
        → "color: red; font-size: 16px;"
    """
    parts = []
    for k, v in props.items():
        css_key = k.replace("_", "-")
        parts.append(f"{css_key}: {v}")
    return "; ".join(parts) + (";" if parts else "")
