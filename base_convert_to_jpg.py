import os
from PIL import Image
import pillow_heif

# Enable HEIC support
pillow_heif.register_heif_opener()

# 🔹 Folder name placed next to this script
FOLDER_NAME = "Identified"   # <-- change this to your folder name

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_PATH = os.path.join(BASE_DIR, FOLDER_NAME)

SUPPORTED_EXT = (".heic", ".png", ".jpeg", ".jpg", ".webp", ".bmp", ".tiff")

for filename in os.listdir(FOLDER_PATH):
    if not filename.lower().endswith(SUPPORTED_EXT):
        continue

    input_path = os.path.join(FOLDER_PATH, filename)
    name, _ = os.path.splitext(filename)
    output_path = os.path.join(FOLDER_PATH, f"{name}.jpg")

    try:
        with Image.open(input_path) as img:
            img = img.convert("RGB")
            img.save(output_path, "JPEG", quality=95)

        # Remove original if different file
        if input_path != output_path:
            os.remove(input_path)

        print(f"Converted: {filename} → {name}.jpg")

    except Exception as e:
        print(f"❌ Failed: {filename} | {e}")
