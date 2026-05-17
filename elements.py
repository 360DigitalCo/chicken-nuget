"""
chicken.elements
~~~~~~~~~~~~~~~~
Every HTML tag as a composable Python object.
Children can be other elements or plain strings.
Keyword args become HTML attributes; trailing underscores are stripped
so `class_="foo"` → class="foo", `for_="id"` → for="id".
"""

from __future__ import annotations
from typing import Any, Union

_VOID = {
    "area","base","br","col","embed","hr","img","input",
    "link","meta","param","source","track","wbr",
}

_INDENT = "  "


class Element:
    tag: str = ""

    def __init__(self, *children: Union["Element", str], **attrs: Any):
        self.children: list[Union[Element, str]] = list(children)
        self.attrs: dict[str, Any] = {
            k.rstrip("_").replace("_", "-"): v
            for k, v in attrs.items()
        }

    # ── fluent helpers ──────────────────────────────────────────────────

    def add(self, *children: Union["Element", str]) -> "Element":
        """Append children and return self for chaining."""
        self.children.extend(children)
        return self

    def attr(self, **kwargs: Any) -> "Element":
        """Set/override attributes and return self."""
        self.attrs.update({
            k.rstrip("_").replace("_", "-"): v
            for k, v in kwargs.items()
        })
        return self

    # ── rendering ───────────────────────────────────────────────────────

    def _attr_str(self) -> str:
        parts = []
        for k, v in self.attrs.items():
            if v is True:
                parts.append(k)
            elif v is False or v is None:
                continue
            else:
                parts.append(f'{k}="{v}"')
        return (" " + " ".join(parts)) if parts else ""

    def render(self, indent: int = 0) -> str:
        pad = _INDENT * indent
        a = self._attr_str()

        if self.tag in _VOID:
            return f"{pad}<{self.tag}{a}>"

        if not self.children:
            return f"{pad}<{self.tag}{a}></{self.tag}>"

        # single inline text child → keep on one line
        if len(self.children) == 1 and isinstance(self.children[0], str):
            return f"{pad}<{self.tag}{a}>{self.children[0]}</{self.tag}>"

        inner = []
        for child in self.children:
            if isinstance(child, str):
                inner.append(_INDENT * (indent + 1) + child)
            else:
                inner.append(child.render(indent + 1))
        body = "\n".join(inner)
        return f"{pad}<{self.tag}{a}>\n{body}\n{pad}</{self.tag}>"

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} tag={self.tag!r} children={len(self.children)}>"


# ── factory ─────────────────────────────────────────────────────────────

def _make(tag: str) -> type:
    return type(tag.capitalize(), (Element,), {"tag": tag})


# document structure
Html    = _make("html")
Head    = _make("head")
Body    = _make("body")
Title   = _make("title")
Base    = _make("base")
Link    = _make("link")
Meta    = _make("meta")
Style   = _make("style")
Script  = _make("script")

# sectioning
Header  = _make("header")
Nav     = _make("nav")
Main    = _make("main")
Article = _make("article")
Section = _make("section")
Aside   = _make("aside")
Footer  = _make("footer")
H1      = _make("h1")
H2      = _make("h2")
H3      = _make("h3")
H4      = _make("h4")
H5      = _make("h5")
H6      = _make("h6")

# grouping
Div     = _make("div")
P       = _make("p")
Ul      = _make("ul")
Ol      = _make("ol")
Li      = _make("li")
Dl      = _make("dl")
Dt      = _make("dt")
Dd      = _make("dd")
Figure  = _make("figure")
Figcaption = _make("figcaption")
Hr      = _make("hr")
Br      = _make("br")
Pre     = _make("pre")
Blockquote = _make("blockquote")

# inline text
A       = _make("a")
Em      = _make("em")
Strong  = _make("strong")
Small   = _make("small")
S       = _make("s")
Cite    = _make("cite")
Code    = _make("code")
Kbd     = _make("kbd")
Samp    = _make("samp")
Var     = _make("var")
Abbr    = _make("abbr")
Span    = _make("span")
Mark    = _make("mark")
Time    = _make("time")
Sub     = _make("sub")
Sup     = _make("sup")

# embedded
Img     = _make("img")
Iframe  = _make("iframe")
Video   = _make("video")
Audio   = _make("audio")
Source  = _make("source")
Canvas  = _make("canvas")
Svg     = _make("svg")

# table
Table   = _make("table")
Caption = _make("caption")
Thead   = _make("thead")
Tbody   = _make("tbody")
Tfoot   = _make("tfoot")
Tr      = _make("tr")
Th      = _make("th")
Td      = _make("td")

# forms
Form    = _make("form")
Label   = _make("label")
Input   = _make("input")
Button  = _make("button")
Select  = _make("select")
Option  = _make("option")
Optgroup = _make("optgroup")
Textarea = _make("textarea")
Fieldset = _make("fieldset")
Legend  = _make("legend")
Datalist = _make("datalist")
Output  = _make("output")
Progress = _make("progress")
Meter   = _make("meter")

# interactive
Details = _make("details")
Summary = _make("summary")
Dialog  = _make("dialog")

# custom / passthrough
Raw = _make("raw")  # renders children only, no wrapper tag

class Raw(Element):  # noqa: F811
    """Inject raw HTML strings without any wrapper element."""
    tag = ""

    def render(self, indent: int = 0) -> str:  # type: ignore[override]
        pad = _INDENT * indent
        parts = []
        for child in self.children:
            if isinstance(child, str):
                parts.append(pad + child)
            else:
                parts.append(child.render(indent))
        return "\n".join(parts)
