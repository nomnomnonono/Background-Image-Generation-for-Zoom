import base64

import numpy as np
import openai
from PIL import Image, ImageDraw, ImageFont

WIDTH = 720
HEIGHT = 1280


def create_with_upload(
    image: np.ndarray,
    name: str,
    org: str,
    name_font_size=50,
    org_font_size=35,
    vspace=50,
    hspace=50,
    between=30,
    red=0,
    green=0,
    blue=100,
) -> np.ndarray:
    """
    アップロードされた画像をもとに背景画像を作成する

    Args:
        image (np.ndarray): アップロード画像
        name (str): 氏名
        org (str): 所属組織
        name_font_size (int, optional): 氏名のフォントサイズ. Defaults to 50.
        org_font_size (int, optional): 組織のフォントサイズ. Defaults to 35.
        vspace (int, optional): 縦方向のスペース. Defaults to 50.
        hspace (int, optional): 横方向のスペース. Defaults to 50.
        between (int, optional): 氏名と組織間のスペース. Defaults to 30.
        red (int, optional): (R,G,B)のRの値. Defaults to 0.
        green (int, optional): (R,G,B)のGの値. Defaults to 0.
        blue (int, optional): (R,G,B)のBの値. Defaults to 100.

    Returns:
        np.ndarray: 背景画像
    """

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
    prompt: str,
    use_before: bool,
    api_key: str,
    name: str,
    org: str,
    name_font_size=50,
    org_font_size=35,
    vspace=50,
    hspace=50,
    between=30,
    red=0,
    green=0,
    blue=100,
) -> np.ndarray:
    """
    生成画像をもとに背景画像を作成する

    Args:
        prompt (str): 画像生成プロンプト
        use_before (bool): 前回生成した画像をそのまま使うか否か
        api_key (str): OpenAI API Key
        name (str): 氏名
        org (str): 所属組織
        name_font_size (int, optional): 氏名のフォントサイズ. Defaults to 50.
        org_font_size (int, optional): 組織のフォントサイズ. Defaults to 35.
        vspace (int, optional): 縦方向のスペース. Defaults to 50.
        hspace (int, optional): 横方向のスペース. Defaults to 50.
        between (int, optional): 氏名と組織間のスペース. Defaults to 30.
        red (int, optional): (R,G,B)のRの値. Defaults to 0.
        green (int, optional): (R,G,B)のGの値. Defaults to 0.
        blue (int, optional): (R,G,B)のBの値. Defaults to 100.

    Returns:
        np.ndarray: 背景画像
    """

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
