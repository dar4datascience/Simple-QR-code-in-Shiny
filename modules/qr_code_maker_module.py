from shiny import module, render, reactive
from shiny.types import ImgData
from shiny.ui import output_image, tags
from shiny_semantic.elements import icon, semantic_input, button, segment
import qrcode
import tempfile


from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
            "Simple Qr Code Maker",
            feature_subsection(
                "Shiny Bound Text Input",
                semantic_input("url_text",
                               placeholder="Place URL", 
                               icon=icon("address card"),
                               semantic_class="large"
                               ),
                button("trigger", "Qrize", icon=icon("hat wizard")),
                tags.br(),
                tags.br(),
                tags.span("QR Code Image:"),
                tags.br(),
                output_image("make_qr_from_url_render",
                                        width='auto',
                                        fill=True),
                
            )
        )

@module.server
def server(input, output, session):

    @reactive.event(input.trigger)
    def make_qr_from_url_reactive():
        if not input.url_text():
            return None

        img = qrcode.make(input.url_text())

        # Create a temporary file
        _, temp_file_name = tempfile.mkstemp()

        # Append .png extension to temp file
        temp_file_name = f"{temp_file_name}_qr_code.png"

        # Save the image to the temporary file
        img.save(temp_file_name)

        img: ImgData = {"src": temp_file_name,
                         "style": """display: flex;
                                   justify-content: center;
                                   align-items: center;
                                   margin: 0 auto;
                                   border-style: double;
                                     """} 

        return img
    
    
    @output
    @render.image()
    def make_qr_from_url_render():
        return make_qr_from_url_reactive()
        
    


