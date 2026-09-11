from pathlib import Path
from PIL import Image

root = Path(r"c:\Users\Sami\Desktop\project")

for name, max_width in [
    ("pic1.jpeg", 1100),
    ("pic2.jpeg", 900),
    ("pic3.jpeg", 900),
]:
    path = root / name
    if not path.exists():
        continue

    with Image.open(path) as img:
        img = img.convert("RGB")
        if img.size[0] > max_width:
            ratio = max_width / img.size[0]
            new_size = (max_width, max(1, int(img.size[1] * ratio)))
            img = img.resize(new_size, Image.LANCZOS)

        img.save(path, format="JPEG", quality=78, optimize=True)
        print(f"Optimized {name} -> {path.stat().st_size / 1024:.1f} KB")
