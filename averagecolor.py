import sys
import os
from PIL import Image

SUPPORTED = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp")
COLOR_SPACE = 256 * 256 * 256
BUCKETS = 100000

def average_color(image_path):
    with Image.open(image_path).convert("RGB") as img:
        pixels = img.getdata()
        r = g = b = count = 0

        for px in pixels:
            r += px[0]
            g += px[1]
            b += px[2]
            count += 1

        return r // count, g // count, b // count

def color_to_bucket(r, g, b):
    color_value = (r << 16) + (g << 8) + b
    bucket = (color_value * BUCKETS) // COLOR_SPACE
    return f"{bucket:05d}"

def rename_file(path):
    if not path.lower().endswith(SUPPORTED):
        return

    try:
        r, g, b = average_color(path)
        prefix = color_to_bucket(r, g, b)

        folder, name = os.path.split(path)

        # Avoid double-prefixing (#####-)
        if name[:5].isdigit() and name[5:6] == "-":
            return

        new_name = f"{prefix}-{name}"
        new_path = os.path.join(folder, new_name)

        if not os.path.exists(new_path):
            os.rename(path, new_path)

    except Exception:
        pass  # intentionally silent

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        rename_file(arg)
