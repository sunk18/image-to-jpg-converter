import io

import streamlit as st
from PIL import Image
import pillow_heif

# Enable HEIC / HEIF support
pillow_heif.register_heif_opener()


SUPPORTED_EXTENSIONS = [
    "heic",
    "heif",
    "png",
    "jpeg",
    "jpg",
    "webp",
    "bmp",
    "tiff",
]


def convert_to_jpg(uploaded_file):
    """
    Convert an uploaded image to JPG and return the JPG bytes.
    """

    with Image.open(uploaded_file) as img:
        img = img.convert("RGB")

        output = io.BytesIO()

        img.save(
            output,
            format="JPEG",
            quality=95
        )

        output.seek(0)

        return output.getvalue()


# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------

st.set_page_config(
    page_title="Image to JPG Converter",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ Image to JPG Converter")

st.write(
    "Upload one or more images and convert them to high-quality JPG files."
)

uploaded_files = st.file_uploader(
    "Choose images",
    type=SUPPORTED_EXTENSIONS,
    accept_multiple_files=True
)


if uploaded_files:

    st.write(f"**{len(uploaded_files)} file(s) selected**")

    for uploaded_file in uploaded_files:

        filename = uploaded_file.name
        name = filename.rsplit(".", 1)[0]

        try:
            jpg_bytes = convert_to_jpg(uploaded_file)

            st.success(f"Converted: {filename} → {name}.jpg")

            st.download_button(
                label=f"⬇️ Download {name}.jpg",
                data=jpg_bytes,
                file_name=f"{name}.jpg",
                mime="image/jpeg",
                key=f"download_{filename}"
            )

        except Exception as e:
            st.error(
                f"❌ Failed to convert {filename}: {str(e)}"
            )