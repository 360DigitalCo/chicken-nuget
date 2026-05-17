r"""
 ___  _  _  _  ___ _  _  ___  _  _     _  _  _  _  ___  ___ _____
/ __|| || || |/ __| || || __|| \| |    | \| || || |/ __|| __||_   _|
| (__ | __ || || (__ | >< || _| | .` |    | .` || || || (_ || _|   | |
\___||_||_||_|\___||_||_||___||_|\_|    |_|\_||_||_|\___||___| |_|

Build HTML with Python. No templates. No regrets.

Usage:
    from chicken import html, head, body, div, p, h1, a
    from chicken import render_page, style

    page = html(
        head(
            meta(charset="utf-8"),
            title("My Page"),
        ),
        body(
            div(class_="container",
                h1("Hello, world!"),
                p("Built with Chicken NuGet."),
                a("Learn more", href="https://github.com/360Digital/chicken-nuget"),
            )
        )
    )

    print(render_page(page))
"""

from .elements import (
    Element,
    Raw,
    # document
    Html as html,
    Head as head,
    Body as body,
    Title as title,
    Base as base,
    Link as link,
    Meta as meta,
    Style as style_el,
    Script as script,
    # sectioning
    Header as header,
    Nav as nav,
    Main as main,
    Article as article,
    Section as section,
    Aside as aside,
    Footer as footer,
    H1 as h1,
    H2 as h2,
    H3 as h3,
    H4 as h4,
    H5 as h5,
    H6 as h6,
    # grouping
    Div as div,
    P as p,
    Ul as ul,
    Ol as ol,
    Li as li,
    Dl as dl,
    Dt as dt,
    Dd as dd,
    Figure as figure,
    Figcaption as figcaption,
    Hr as hr,
    Br as br,
    Pre as pre,
    Blockquote as blockquote,
    # inline
    A as a,
    Em as em,
    Strong as strong,
    Small as small,
    S as s,
    Cite as cite,
    Code as code,
    Kbd as kbd,
    Samp as samp,
    Var as var,
    Abbr as abbr,
    Span as span,
    Mark as mark,
    Time as time,
    Sub as sub,
    Sup as sup,
    # embedded
    Img as img,
    Iframe as iframe,
    Video as video,
    Audio as audio,
    Source as source,
    Canvas as canvas,
    Svg as svg,
    # table
    Table as table,
    Caption as caption,
    Thead as thead,
    Tbody as tbody,
    Tfoot as tfoot,
    Tr as tr,
    Th as th,
    Td as td,
    # forms
    Form as form,
    Label as label,
    Input as input_,
    Button as button,
    Select as select,
    Option as option,
    Optgroup as optgroup,
    Textarea as textarea,
    Fieldset as fieldset,
    Legend as legend,
    Datalist as datalist,
    Output as output,
    Progress as progress,
    Meter as meter,
    # interactive
    Details as details,
    Summary as summary,
    Dialog as dialog,
)

from .render import render, render_page, to_file, style

__version__ = "0.1.0"
__author__  = "360Digital, Co."
__all__ = [
    # core
    "Element", "Raw",
    # render helpers
    "render", "render_page", "to_file", "style",
    # tags (all lowercase)
    "html","head","body","title","base","link","meta","style_el","script",
    "header","nav","main","article","section","aside","footer",
    "h1","h2","h3","h4","h5","h6",
    "div","p","ul","ol","li","dl","dt","dd",
    "figure","figcaption","hr","br","pre","blockquote",
    "a","em","strong","small","s","cite","code","kbd","samp",
    "var","abbr","span","mark","time","sub","sup",
    "img","iframe","video","audio","source","canvas","svg",
    "table","caption","thead","tbody","tfoot","tr","th","td",
    "form","label","input_","button","select","option","optgroup",
    "textarea","fieldset","legend","datalist","output","progress","meter",
    "details","summary","dialog",
]
