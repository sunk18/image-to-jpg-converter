# Image to JPG Converter

A simple Streamlit-based web application that converts images from multiple formats into high-quality JPG files.

The application supports common image formats including **HEIC, HEIF, PNG, JPEG, JPG, WEBP, BMP, and TIFF**.

## Features

* Convert multiple images in one go
* HEIC/HEIF support
* Converts images to RGB JPG
* JPEG quality set to 95
* Preserves the original filename
* Download each converted JPG individually
* Runs locally or can be deployed using Streamlit Community Cloud
* No files need to be stored permanently on the server

## Supported Input Formats

The application supports:

* `.heic`
* `.heif`
* `.png`
* `.jpeg`
* `.jpg`
* `.webp`
* `.bmp`
* `.tiff`

All supported images are converted to:

```text
.jpg
```

## Project Structure

```text
image-to-jpg-converter/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit application and image conversion logic.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `README.md`

Contains project documentation, setup instructions, testing instructions, and usage information.

---

# Local Setup

## Prerequisites

Make sure the following are installed:

* Python 3.10 or later
* Git
* Internet connection for installing Python packages

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

## 1. Clone the Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/image-to-jpg-converter.git
```

Move into the project directory:

```bash
cd image-to-jpg-converter
```

## 2. Create a Virtual Environment

Creating a virtual environment is recommended so that the application's dependencies do not interfere with other Python projects.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, your terminal should show something similar to:

```text
(venv)
```

## 3. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

The required packages are:

```text
streamlit
Pillow
pillow-heif
```

---

# Run the Application Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will normally start the application at:

```text
http://localhost:8501
```

Open that address in your browser.

If Streamlit provides a different URL in the terminal, use the URL displayed there.

---

# Application Usage

## Step 1 — Open the Application

Launch the application using:

```bash
streamlit run app.py
```

Open the displayed local URL in your browser.

## Step 2 — Upload Images

Click:

```text
Browse files
```

Select one or more supported image files.

Multiple files can be selected at the same time.

For example:

```text
photo1.heic
photo2.png
photo3.webp
photo4.tiff
```

## Step 3 — Conversion

The application automatically converts each uploaded image into JPG format.

For example:

```text
photo1.heic  →  photo1.jpg
photo2.png   →  photo2.jpg
photo3.webp  →  photo3.jpg
```

Images are converted to RGB before being saved as JPG.

JPEG quality is configured to:

```text
95
```

## Step 4 — Download

After successful conversion, a download button is displayed for each file.

Click:

```text
Download <filename>.jpg
```

to save the converted image to your computer.

---

# Testing Instructions

Before deploying the application, test the supported formats locally.

## Basic Test

Upload a JPG file.

Expected result:

```text
input.jpg → input.jpg
```

The application should successfully process the file and provide a download option.

## PNG Test

Upload:

```text
sample.png
```

Expected result:

```text
sample.png → sample.jpg
```

The resulting file should be a valid JPG image.

## HEIC Test

Upload:

```text
sample.heic
```

Expected result:

```text
sample.heic → sample.jpg
```

This test confirms that HEIC support through `pillow-heif` is working correctly.

## WEBP Test

Upload:

```text
sample.webp
```

Expected result:

```text
sample.webp → sample.jpg
```

## TIFF Test

Upload:

```text
sample.tiff
```

Expected result:

```text
sample.tiff → sample.jpg
```

## Multiple File Test

Select several different image formats at the same time.

For example:

```text
photo1.heic
photo2.png
photo3.webp
photo4.jpeg
photo5.tiff
```

Expected result:

* All supported files are processed.
* Each file receives a JPG download option.
* Original filenames are retained.
* One failed conversion should not prevent other files from being processed.

## Invalid File Test

Try uploading an unsupported file type such as:

```text
document.pdf
test.txt
file.docx
```

Expected result:

The application should not allow unsupported file types to be selected.

## Image Quality Test

After downloading a converted JPG:

1. Open the image.
2. Verify that it can be opened normally.
3. Compare it with the original.
4. Verify that the image dimensions are retained.
5. Verify that there is no unexpected rotation or corruption.

---

# Error Handling

If an individual image cannot be converted, the application displays an error for that file.

For example:

```text
❌ Failed to convert: sample.heic
```

Other successfully uploaded files should continue to be processed.

Common causes of conversion failure include:

* Corrupted image
* Invalid image format
* Unsupported image encoding
* Damaged HEIC/HEIF file

---

# Important Behaviour

The application processes uploaded files temporarily.

It does **not** depend on an `Identified` folder or any fixed folder on the user's computer.

Unlike the original desktop script, the application does not delete the original files from the user's computer.

The original files remain unchanged.

The user downloads the converted JPG separately.

---

# Streamlit Deployment

The application can be deployed using Streamlit Community Cloud directly from GitHub.

The repository should contain at least:

```text
app.py
requirements.txt
README.md
```

When creating the Streamlit application, configure:

```text
Repository: <YOUR_USERNAME>/image-to-jpg-converter
Branch: main
Main file: app.py
```

Streamlit will install the dependencies listed in:

```text
requirements.txt
```

and start the application.

## Deployment Checklist

Before deployment, verify:

* [ ] `app.py` exists in the repository root
* [ ] `requirements.txt` exists
* [ ] All required packages are listed in `requirements.txt`
* [ ] Application runs successfully with `streamlit run app.py`
* [ ] HEIC conversion works locally
* [ ] Multiple file upload works
* [ ] JPG download works
* [ ] Changes have been committed and pushed to GitHub

---

# Updating the Application

After making changes locally:

```bash
git add .
git commit -m "Update image converter"
git push
```

If the application is already deployed through Streamlit Community Cloud, the deployment will normally detect the updated GitHub repository and redeploy the application.

---

# Dependencies

The application uses:

| Package     | Purpose                             |
| ----------- | ----------------------------------- |
| Streamlit   | Web application UI                  |
| Pillow      | Image processing and JPG conversion |
| pillow-heif | HEIC/HEIF image support             |

---

# License

Add the appropriate license here if this repository is intended to be shared publicly.
