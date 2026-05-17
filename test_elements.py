"""
Tests for chicken_nuget elements and render utilities.
Run with: python -m pytest tests/
"""
import pytest
from chicken import (
    html, head, body, div, p, h1, h2, a, span, img, br, hr,
    ul, li, form, input_, button, meta, link, title, script, style_el,
    render, render_page, to_file, style, Raw
)


# ── Element basics ───────────────────────────────────────────────────────

class TestElement:
    def test_simple_tag(self):
        assert p("hello").render() == "<p>hello</p>"

    def test_nested(self):
        out = div(p("hi")).render()
        assert "<div>" in out
        assert "<p>hi</p>" in out

    def test_attrs(self):
        out = a("click", href="https://example.com").render()
        assert 'href="https://example.com"' in out

    def test_class_underscore(self):
        out = div(class_="foo bar").render()
        assert 'class="foo bar"' in out

    def test_boolean_attr_true(self):
        out = input_(disabled=True).render()
        assert "disabled" in out
        assert "True" not in out

    def test_boolean_attr_false(self):
        out = input_(disabled=False).render()
        assert "disabled" not in out

    def test_void_element_no_close(self):
        out = br().render()
        assert out == "<br>"
        assert "</br>" not in out

    def test_hr_void(self):
        assert img(src="a.png", alt="").render() == '<img src="a.png" alt="">'

    def test_add_chainable(self):
        d = div()
        d.add(p("a")).add(p("b"))
        out = d.render()
        assert "<p>a</p>" in out
        assert "<p>b</p>" in out

    def test_attr_chainable(self):
        el = div().attr(id="box", class_="main")
        out = el.render()
        assert 'id="box"' in out
        assert 'class="main"' in out

    def test_empty_element(self):
        out = div().render()
        assert out == "<div></div>"

    def test_hyphen_attr(self):
        out = div(data_value="42").render()
        assert 'data-value="42"' in out

    def test_multiple_children(self):
        out = ul(li("a"), li("b"), li("c")).render()
        assert out.count("<li>") == 3

    def test_str_coercion(self):
        assert str(p("x")) == "<p>x</p>"

    def test_repr(self):
        r = repr(div(p("hi")))
        assert "Div" in r or "div" in r.lower()

    def test_mixed_children(self):
        out = p("Hello ", span("world"), "!").render()
        assert "Hello" in out
        assert "<span>world</span>" in out


# ── Raw element ──────────────────────────────────────────────────────────

class TestRaw:
    def test_raw_passthrough(self):
        out = Raw("<!-- comment -->").render()
        assert out == "<!-- comment -->"

    def test_raw_no_wrapper(self):
        out = Raw("<b>bold</b>").render()
        assert "<raw>" not in out

    def test_raw_inside_div(self):
        out = div(Raw("<hr>")).render()
        assert "<hr>" in out
        assert "<div>" in out


# ── Render helpers ───────────────────────────────────────────────────────

class TestRender:
    def test_render_basic(self):
        out = render(p("hi"))
        assert out == "<p>hi</p>"

    def test_render_with_doctype(self):
        out = render(html(), doctype=True)
        assert out.startswith("<!DOCTYPE html>")

    def test_render_page(self):
        out = render_page(html())
        assert "<!DOCTYPE html>" in out

    def test_minify(self):
        out = render(div(p("hello")), minify=True)
        assert "\n" not in out
        assert "  " not in out

    def test_to_file(self, tmp_path):
        f = tmp_path / "out.html"
        to_file(p("hello"), str(f))
        content = f.read_text()
        assert "<!DOCTYPE html>" in content
        assert "<p>hello</p>" in content


# ── style() helper ───────────────────────────────────────────────────────

class TestStyle:
    def test_basic(self):
        out = style(color="red", font_size="16px")
        assert "color: red" in out
        assert "font-size: 16px" in out
        assert out.endswith(";")

    def test_underscore_to_hyphen(self):
        out = style(background_color="#fff")
        assert "background-color: #fff" in out

    def test_empty(self):
        out = style()
        assert out == ""


# ── Integration: full page ───────────────────────────────────────────────

class TestIntegration:
    def test_full_page(self):
        page = html(
            head(
                meta(charset="utf-8"),
                title("Test"),
                link(rel="stylesheet", href="style.css"),
            ),
            body(
                div(
                    h1("Hello"),
                    p("World"),
                    a("Click", href="#"),
                    class_="wrapper",
                )
            )
        )
        out = render_page(page)
        assert "<!DOCTYPE html>" in out
        assert "<h1>Hello</h1>" in out
        assert 'class="wrapper"' in out
        assert 'charset="utf-8"' in out

    def test_form(self):
        f = form(
            input_(type="text", name="q", placeholder="Search"),
            button("Go", type="submit"),
            method="get", action="/search"
        )
        out = f.render()
        assert 'method="get"' in out
        assert 'placeholder="Search"' in out
        assert "<button" in out

    def test_table(self):
        from chicken import table, thead, tbody, tr, th, td
        t = table(
            thead(tr(th("Name"), th("Score"))),
            tbody(
                tr(td("Alice"), td("95")),
                tr(td("Bob"),   td("87")),
            )
        )
        out = t.render()
        assert "<table>" in out
        assert "<th>Name</th>" in out
        assert "<td>Alice</td>" in out
