import importlib
import io
import os

import qrcode
from PIL import Image, ImageDraw, ImageFont


def gen_qr_png_data(maildomain):
    url = f"DCACCOUNT:https://{maildomain}/new"
    image = gen_qr(maildomain, url)
    temp = io.BytesIO()
    image.save(temp, format="png")
    temp.seek(0)
    return temp


def gen_qr(maildomain, url):
    # taken and modified from
    # https://github.com/deltachat/mailadm/blob/master/src/mailadm/gen_qr.py

    # info = f"{maildomain} invite code"
    info = ""

    # load QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=1,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # paint all elements
    ttf_path = str(
        importlib.resources.files(__package__).joinpath("data/opensans-regular.ttf")
    )

    assert os.path.exists(ttf_path), ttf_path
    font_size = 16
    font = ImageFont.truetype(font=ttf_path, size=font_size)

    num_lines = ((info).count("\n") + 1) if info else 0

    size = width = 384
    qr_padding = 6
    text_height = font_size * num_lines
    height = size + text_height

    image = Image.new("RGBA", (width, height), "white")
    qr_final_size = width - (qr_padding * 2)

    if num_lines:
        draw = ImageDraw.Draw(image)

        # draw text
        if hasattr(font, "getsize"):
            info_pos = (width - font.getsize(info.strip())[0]) // 2
        else:
            info_pos = (width - font.getbbox(info.strip())[3]) // 2

        draw.multiline_text(
            (info_pos, size - qr_padding // 2),
            info,
            font=font,
            fill="black",
            align="right",
        )

    # paste QR code
    image.paste(
        qr_img.resize((qr_final_size, qr_final_size), resample=Image.NEAREST),
        (qr_padding, qr_padding),
    )

    # center chatmail "@" logo on a white card so it stays scannable
    logo_size = int(size / 6)
    logo = Image.new("RGBA", (logo_size, logo_size), (255, 255, 255, 255))
    logo_draw = ImageDraw.Draw(logo)
    logo_font = ImageFont.truetype(font=ttf_path, size=int(logo_size * 0.85))
    logo_draw.text(
        (logo_size // 2, logo_size // 2),
        "@",
        anchor="mm",
        font=logo_font,
        fill="black",
    )
    pos = int((size / 2) - (logo_size / 2))
    image.paste(logo, (pos, pos), mask=logo)

    return image
