"""Draws the favicon files and the social sharing image (og-image.jpg) in the site's light style."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
INK, ACCENT, BG = (28, 25, 23), (249, 115, 22), (251, 248, 243)


def font(size, bold=True):
    names = ["segoeuib.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return ImageFont.load_default()


def mono(size):
    for n in ["consolab.ttf", "CascadiaCode.ttf", "cour.ttf"]:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return font(size)


# favicon.svg: dark rounded square, "TW", orange dot (same as the nav mark)
(ROOT / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#1C1917"/>'
    '<text x="30" y="41" text-anchor="middle" font-family="Consolas, Menlo, monospace" font-size="24" font-weight="700" fill="#fff">TW</text>'
    '<circle cx="52" cy="52" r="5" fill="#F97316"/></svg>\n', encoding="utf-8")


def mark(size):
    s = size * 4                                    # draw big, then shrink for smooth edges
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=s // 4, fill=INK)
    f = mono(int(s * .38))
    d.text((s * .47, s * .5), "TW", font=f, fill="white", anchor="mm")
    r = s * .08
    d.ellipse([s * .81 - r, s * .81 - r, s * .81 + r, s * .81 + r], fill=ACCENT)
    return im.resize((size, size), Image.LANCZOS)


mark(32).save(ROOT / "favicon-32.png")
mark(180).save(ROOT / "apple-touch-icon.png")

# og-image.jpg: 1200x630
W, H = 1200, 630
og = Image.new("RGB", (W, H), BG)
glow = Image.new("RGB", (W, H), BG)
g = ImageDraw.Draw(glow)
g.ellipse([760, -160, 1300, 380], fill=(255, 217, 184))
g.ellipse([820, 360, 1240, 780], fill=(207, 239, 226))
g.ellipse([-160, 380, 260, 800], fill=(227, 224, 251))
og = glow.filter(ImageFilter.GaussianBlur(90))
d = ImageDraw.Draw(og)
for x in range(0, W, 26):                           # dot grid
    for y in range(0, H, 26):
        d.ellipse([x, y, x + 2.4, y + 2.4], fill=(228, 218, 203))
d.rounded_rectangle([72, 70, 128, 126], radius=14, fill=INK)
d.text((98, 98), "TW", font=mono(22), fill="white", anchor="mm")
d.ellipse([113, 111, 122, 120], fill=ACCENT)
d.text((146, 98), "Tadrous William", font=font(30), fill=INK, anchor="lm")
d.text((72, 200), "I build AI chatbots and", font=font(64), fill=INK)
d.text((72, 276), "ML models that are ", font=font(64), fill=INK)
w = d.textlength("ML models that are ", font=font(64))
d.text((72 + w, 276), "tested.", font=font(64), fill=(194, 65, 12))
d.line([(76 + w, 356), (72 + w + d.textlength("tested.", font=font(64)), 352)], fill=ACCENT, width=6)
d.text((72, 384), "AI Engineer & Data Scientist  ·  RAG chatbots  ·  ML  ·  Dashboards", font=font(26, bold=False), fill=(87, 83, 78))
x = 72
for big, small in [("100%", "Job Success"), ("5.0", "rating"), ("3rd", "place nationally"), ("30/30", "chatbot test")]:
    bw = max(d.textlength(big, font=font(40)), d.textlength(small, font=font(20, bold=False))) + 44
    d.rounded_rectangle([x, 462, x + bw, 560], radius=18, fill="white", outline=(234, 223, 207), width=2)
    d.text((x + 22, 476), big, font=font(40), fill=INK)
    d.text((x + 22, 526), small, font=font(20, bold=False), fill=(120, 113, 108))
    x += bw + 16
og.save(ROOT / "og-image.jpg", quality=86, optimize=True, progressive=True)
print("icons and og-image written")
