import numpy as np
from PIL import Image, ImageDraw, ImageFont

WIDTH = 720
HEIGHT = 1280


def generate(
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
