from shiny import App
from shiny.ui import tags

from shiny_semantic import page_semantic

import modules
from app_layout import header, hero, sidebar
from pathlib import Path


app_ui = page_semantic(
    header(),
    sidebar(),
    tags.div(
      hero(),
         modules.qr_code_maker.ui("qr_code_maker_section"),
         tags.div(style="opacity: 0; height: 5rem;"),
    ),
    title="Shiny QR Code Maker Demo",
)


def app_server(input, output, session):
    modules.qr_code_maker.server("qr_code_maker_section")
    

www_dir = Path(__file__).parent / "www"
app = App(ui=app_ui, server=app_server, static_assets=www_dir)