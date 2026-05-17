"""
examples/page_builder.py
~~~~~~~~~~~~~~~~~~~~~~~~~
Reusable component pattern with Chicken NuGet.
"""

from chicken import (
    html, head, body, div, header, main, footer,
    nav, ul, li, a, h1, h2, p, span, meta, title, style_el,
    render_page, style, Raw
)


# ── Reusable components ──────────────────────────────────────────────────

def navbar(brand: str, links: list[tuple[str, str]]):
    return header(
        nav(
            span(brand, style=style(font_weight="bold", font_size="1.2rem")),
            ul(
                *[li(a(label, href=href)) for label, href in links],
                style=style(display="flex", gap="1.5rem", list_style="none", margin="0", padding="0"),
            ),
            style=style(
                display="flex",
                justify_content="space-between",
                align_items="center",
                padding="0.75rem 1.5rem",
                background="#1a1a1a",
                color="#fff",
            )
        )
    )


def hero(headline: str, sub: str, cta_label: str, cta_href: str):
    return div(
        h1(headline),
        p(sub),
        a(cta_label, href=cta_href,
          style=style(
              display="inline-block",
              background="#cc7722",
              color="#fff",
              padding="0.6rem 1.4rem",
              text_decoration="none",
              border_radius="4px",
              font_weight="bold",
          )),
        style=style(
            text_align="center",
            padding="4rem 1rem",
            background="#fffbe6",
        )
    )


def card(title_text: str, body_text: str):
    return div(
        h2(title_text, style=style(margin_top="0")),
        p(body_text),
        style=style(
            border="1px solid #ddd",
            border_radius="6px",
            padding="1.25rem",
            background="#fff",
        )
    )


def page_footer(text: str):
    return footer(
        p(text),
        style=style(
            text_align="center",
            padding="1rem",
            background="#1a1a1a",
            color="#aaa",
            font_size="0.85rem",
            margin_top="3rem",
        )
    )


# ── Compose the page ────────────────────────────────────────────────────

page = html(
    head(
        meta(charset="utf-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        title("Chicken NuGet — Page Builder"),
        style_el("""
            * { box-sizing: border-box; }
            body { margin: 0; font-family: Courier New, monospace; background: #f5f5f0; color: #222; }
            .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
        """),
    ),
    body(
        navbar("🐔 NuGet", [
            ("Docs",    "/docs"),
            ("GitHub",  "https://github.com/360Digital/chicken-nuget"),
            ("PyPI",    "https://pypi.org"),
        ]),
        hero(
            "HTML is just Python objects.",
            "Chicken NuGet turns every HTML tag into a composable, chainable Python class.",
            "Get started →",
            "https://github.com/360Digital/chicken-nuget",
        ),
        main(
            div(class_="cards",
                card("Zero dependencies", "Pure Python. No Jinja, no Mako, no template files. Just import and build."),
                card("Composable",        "Elements are objects — pass them around, return them from functions, store them in lists."),
                card("Readable",          "Your Python code looks like your HTML. Indented, nested, and clear."),
                card("Void-aware",        "<br>, <img>, <input> and friends render without closing tags. Automatically."),
                card("Style helper",      "style(font_size='16px') → 'font-size: 16px;'. Underscores to hyphens, no fuss."),
                card("File output",       "to_file(page, 'index.html') and you're done. Static site generation in 3 lines."),
            ),
            style=style(max_width="960px", margin="3rem auto", padding="0 1rem"),
        ),
        page_footer("© 2025 360Digital, Co. — Made with Chicken NuGet"),
    )
)

if __name__ == "__main__":
    print(render_page(page))
