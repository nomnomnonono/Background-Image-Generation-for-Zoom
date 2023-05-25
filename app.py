import gradio as gr
from src.create import create_with_generate, create_with_upload


def main() -> None:
    """アプリケーション実行関数"""

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
                    name_size = gr.Number(
                        precision=0, value=50, label="Font size of name"
                    )
                with gr.Row():
                    hspace = gr.Number(precision=0, value=50, label="Horizontal space")
                    vspace = gr.Number(precision=0, value=50, label="Vertical space")
                    interval_space = gr.Number(
                        precision=0, value=30, label="Interval space"
                    )
                red = gr.Slider(maximum=255, minimum=0, step=1, value=0, label="Red")
                green = gr.Slider(maximum=255, minimum=0, step=1, value=0, label="Blue")
                blue = gr.Slider(
                    maximum=255, minimum=0, step=1, value=100, label="Green"
                )

                with gr.TabItem(label="Upload image"):
                    image_input = gr.Image(label="Input imgae")
                    upload_button = gr.Button("Generate")
                with gr.TabItem(label="Generate image"):
                    with gr.Row():
                        api_key = gr.Textbox(label="You own OpenAI API key")
                        use_before = gr.Radio(
                            ["Generate new one", "Use before one"],
                            value="Generate new one",
                        )
                    prompt = gr.Textbox(
                        value="background image for zoom meeting",
                        label="Prompt message to generate image",
                    )
                    generate_button = gr.Button("Generate")
            with gr.Column(scale=1):
                image_output = gr.Image(label="Output image")

        upload_button.click(
            create_with_upload,
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

        generate_button.click(
            create_with_generate,
            inputs=[
                prompt,
                use_before,
                api_key,
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


if __name__ == "__main__":
    main()
