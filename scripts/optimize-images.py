#!/usr/bin/env python3
"""Otimiza imagens de context/images para frontend/assets/images (WebP + JPG fallback)."""
import pathlib
from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "context" / "images"
DST = ROOT / "frontend" / "assets" / "images"
MAXW = 1280

# Curadoria: fotos profissionais boas para carrossel/hero.
PHOTOS = ["photo_1", "photo_02", "photo_03", "photo_04", "photo_05",
          "photo_06", "photo_07", "photo_08", "photo_09", "photo_10"]
HERO = "photo_1"  # foto de destaque do hero
# Posts curados para o carrossel do Instagram (na ordem desejada).
POSTS = [f"post_{n:02d}" for n in range(1, 18)]

def save(src_path: pathlib.Path, out_base: pathlib.Path):
    img = ImageOps.exif_transpose(Image.open(src_path)).convert("RGB")
    if img.width > MAXW:
        h = round(img.height * MAXW / img.width)
        img = img.resize((MAXW, h), Image.LANCZOS)
    out_base.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_base.with_suffix(".webp"), "WEBP", quality=82, method=6)
    img.save(out_base.with_suffix(".jpg"), "JPEG", quality=82, optimize=True, progressive=True)
    print("ok:", out_base.name)

for name in PHOTOS:
    save(SRC / f"{name}.jpeg", DST / "photos" / name)
save(SRC / f"{HERO}.jpeg", DST / "hero" / "hero")
for name in POSTS:
    save(SRC / f"{name}.jpeg", DST / "posts" / name)
print("Concluído.")
