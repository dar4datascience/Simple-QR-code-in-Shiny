from shiny.ui import tags

from shiny_semantic.elements import container, segment


def header():
    onclick_callback = """
        $('.ui.sidebar')
            .sidebar({
                transition: 'overlay',
                dimPage: true,
                blurring: true,
            })
            .sidebar('toggle');
    """

    return (
        tags.div(
            tags.div(
                "Shiny for Python",
                class_="ui header item",
            ),
            tags.div(
                tags.i(class_="hamburger icon"),
                class_="ui basic icon button item",
                onclick=onclick_callback,
            ),
            tags.div(
                "Built by DAR4DS",
                class_="right floating item",
            ),
            class_="ui top fixed menu",
            style="z-index: 103;",
        ),
    )


def hero():
    title = tags.h1(
        "Shiny Semantic: Components QR Code Maker Demo",
        class_="ui inverted header",
        style="margin-block: 4em;",
    )

    hero = segment(
        container(title, class_="text"),
        class_="inverted vertical masthead center aligned",
    )
    return hero


def sidebar():
    def _link(item):
        return tags.a(
            item,
            href=f"#{item}",
            class_="item",
            onclick="$('.ui.sidebar').sidebar('toggle');",
        )

    return (
        tags.div(
            _link("Simple Qr Code Maker"),
            class_="ui left vertical menu inverted sidebar",
            style="padding-top: 4rem;",
        ),
    )
