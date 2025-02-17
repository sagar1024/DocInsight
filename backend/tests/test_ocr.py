#Using this small streamlit website to check if OCR is working properly
#Got the error
#Installed tesseract and now its working

import io
import cv2
import numpy as np
import pytesseract
from PIL import Image
import fitz  # PyMuPDF for PDF processing
import streamlit as st

def preprocess_image(image):
    """
    Preprocess the image to improve OCR accuracy.
    - Convert to grayscale
    - Resize
    - Apply adaptive threshold
    """
    # Convert to grayscale
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Rescale the image
    scale_factor = 2  # Rescale to double size
    height, width = gray.shape[:2]
    resized = cv2.resize(gray, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Denoise the image
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

    return Image.fromarray(denoised)

def extract_text_from_image(image):
    """
    Extract text from an image using OCR.
    """
    processed_image = preprocess_image(image)
    extracted_text = pytesseract.image_to_string(processed_image)
    return extracted_text

def extract_text_from_pdf(file):
    """
    Extract text from all pages and images in a PDF.
    """
    text_content = ""
    image_text_content = ""

    pdf_document = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf_document:
        # Extract text from the page
        text_content += page.get_text("text") + "\n"

        # Extract images from the page and perform OCR
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))

            # Extract text from the image
            extracted_text = extract_text_from_image(image)
            image_text_content += extracted_text + "\n"

    combined_text = text_content + "\n" + image_text_content
    return combined_text

# Streamlit App to Upload and Test OCR
def main():
    st.title("OCR Testing for Document Processing")
    
    # File upload input
    uploaded_file = st.file_uploader("Upload a PDF or Image file for OCR testing", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # If the uploaded file is a PDF, extract text from it
        if uploaded_file.name.endswith(".pdf"):
            with st.spinner("Extracting text from PDF..."):
                extracted_text = extract_text_from_pdf(uploaded_file)
                st.text_area("Extracted Text", extracted_text, height=400)
        else:
            # For image files, extract text directly
            image = Image.open(uploaded_file)
            with st.spinner("Extracting text from image..."):
                extracted_text = extract_text_from_image(image)
                st.text_area("Extracted Text", extracted_text, height=400)

if __name__ == "__main__":
    main()
