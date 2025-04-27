import streamlit as st
from PIL import Image
from ocr_module import extract_text_from_image
from summarizer_module import summarize_text

st.set_page_config(page_title="📝 Text & Image Summarizer", layout="centered")

st.title("🧠 Text & Image Summarizer")
st.write("Upload an image or paste text to get a summarized version.")

input_type = st.radio("Choose Input Type:", ["Text", "Image"])

text_input = ""

if input_type == "Text":
    text_input = st.text_area("Enter your text here:", height=200)
else:
    uploaded_file = st.file_uploader("Upload an image (JPEG/PNG)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        with st.spinner("Extracting text..."):
            text_input = extract_text_from_image(image)
        st.text_area("Extracted Text:", text_input, height=200)

if st.button("Summarize"):
    if text_input:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_input)
        st.subheader("Summary")
        st.success(summary)
    else:
        st.warning("Please enter or upload some text first.")
