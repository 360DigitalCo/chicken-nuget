"""
examples/basic.py
~~~~~~~~~~~~~~~~~
Quick intro to chicken_nuget.
Run: python examples/basic.py > output.html
"""

from chicken import (
    html, head, body, div, p, h1, h2, a, ul, li,
    meta, title, link, style_el,
    render_page, style
)

page = html(
    head(
        meta(charset="utf-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        title("Chicken NuGet — Basic Example"),
        style_el("""
            body { font-family: Courier New, monospace; max-width: 640px; margin: 2rem auto; padding: 0 1rem; }
            h1   { color: #cc7722; }
            a    { color: #226699; }
        """),
    ),
    body(
        h1("🐔 Chicken NuGet"),
        p("Build HTML with Python. No templates. No regrets."),
        h2("Features"),
        ul(
            li("Every HTML tag as a Python object"),
            li("Chainable .add() and .attr() methods"),
            li(a("Inline style() helper", href="#style")),
            li("Void elements rendered correctly (br, img, input…)"),
            li("class_ / for_ → class / for (no keyword clashes)"),
        ),
        div(id="style",
            style=style(
                background="#fffbe6",
                border="1px solid #cc7722",
                padding="1rem",
                border_radius="4px",
                margin_top="1.5rem",
            ),
            *[p("This box's style was built with the style() helper.")]
        ),
        p(
            a("GitHub", href="https://github.com/360Digital/chicken-nuget"),
            " · Made with ❤️ and Courier New",
        ),
    )
)

if __name__ == "__main__":
    print(render_page(page))
