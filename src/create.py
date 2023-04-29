import base64

import numpy as np
import openai
from PIL import Image, ImageDraw, ImageFont

WIDTH = 720
HEIGHT = 1280


def create_with_upload(
    image,
    name,
    org,
    name_font_size=50,
    org_font_size=35,
    vspace=50,
    hspace=50,
    between=30,
    red=0,
    green=0,
    blue=100,
):
    img = Image.fromarray(image).resize((HEIGHT, WIDTH), resample=Image.BICUBIC)
    name_font = ImageFont.truetype("ヒラギノ丸ゴ ProN W4.ttc", name_font_size)
    org_font = ImageFont.truetype("ヒラギノ丸ゴ ProN W4.ttc", org_font_size)
    draw = ImageDraw.Draw(img)
    draw.text((hspace, vspace), org, (red, green, blue), font=org_font)
    draw.text(
        (hspace, vspace + org_font_size + between),
        name,
        (red, green, blue),
        font=name_font,
    )
    return np.array(img)


def create_with_generate(
    prompt,
    use_before,
    api_key,
    name,
    org,
    name_font_size=50,
    org_font_size=35,
    vspace=50,
    hspace=50,
    between=30,
    red=0,
    green=0,
    blue=100,
):
    openai.api_key = api_key
    if use_before == "Generate new one":
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json",
        )
        img_data = base64.b64decode(response["data"][0]["b64_json"])
        with open("tmp.png", "wb") as f:
            f.write(img_data)

    img = Image.open("tmp.png").resize((HEIGHT, WIDTH), resample=Image.BICUBIC)
    name_font = ImageFont.truetype("ヒラギノ丸ゴ ProN W4.ttc", name_font_size)
    org_font = ImageFont.truetype("ヒラギノ丸ゴ ProN W4.ttc", org_font_size)
    draw = ImageDraw.Draw(img)
    draw.text((hspace, vspace), org, (red, green, blue), font=org_font)
    draw.text(
        (hspace, vspace + org_font_size + between),
        name,
        (red, green, blue),
        font=name_font,
    )
    return np.array(img)
