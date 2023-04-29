import gradio as gr
from src.generate import generate

with gr.Blocks() as demo:
    gr.Markdown("Generate background imgage for zoom using this demo.")
    with gr.Row():
        with gr.Column(scale=1):
            with gr.Row():
                organization = gr.Textbox(label="Your organization")
                name = gr.Textbox(label="Your name")
            with gr.Row():
                organization_size = gr.Number(
                    precision=0, value=35, label="Font size of organization"
                )
                name_size = gr.Number(precision=0, value=50, label="Font size of name")
            with gr.Row():
                hspace = gr.Number(precision=0, value=50, label="Horizontal space")
                vspace = gr.Number(precision=0, value=50, label="Vertical space")
                interval_space = gr.Number(
                    precision=0, value=30, label="Interval space"
                )
            red = gr.Slider(maximum=255, minimum=0, step=1, value=0, label="Red")
            green = gr.Slider(maximum=255, minimum=0, step=1, value=0, label="Blue")
            blue = gr.Slider(maximum=255, minimum=0, step=1, value=100, label="Green")

            image_input = gr.Image(label="Input imgae")
            button = gr.Button("Generate")
        with gr.Column(scale=1):
            image_output = gr.Image(label="Output image")

    button.click(
        generate,
        inputs=[
            image_input,
            name,
            organization,
            name_size,
            organization_size,
            vspace,
            hspace,
            interval_space,
            red,
            green,
            blue,
        ],
        outputs=image_output,
    )

demo.launch()
