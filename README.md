# Text-Summarizer-
An NLP-powered text summarizer that generates concise summaries from large texts with extractive and abstractive techniques.



# 🧠 Text & Image Summarizer

## ✨ Features
- Summarize plain text entered by the user.
- Extract text from uploaded images (JPEG/PNG) using Tesseract OCR and summarize it.
- Fast and accurate summarization using the **facebook/bart-large-cnn** model.
- Simple, clean, and interactive web interface.

## 🚀 Demo
Upload an image or paste your text, and instantly get a summarized version!

## 📦 Technologies Used
- [Streamlit](https://streamlit.io/) — for the web interface.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) — for extracting text from images.
- [Transformers by HuggingFace](https://huggingface.co/transformers/) — for text summarization (`facebook/bart-large-cnn` model).
- [PyTorch](https://pytorch.org/) — underlying framework for model execution.

## 📂 Project Structure
```
.
├── app.py                # Streamlit app main script
├── ocr_module.py         # OCR text extraction module
├── summarizer_module.py  # Text summarization module
```

## 🛠️ Setup Instructions
### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install required dependencies:
```bash
pip install -r requirements.txt
```

**Example `requirements.txt`**
```
streamlit
pillow
pytesseract
torch
transformers
```

### 3. (Optional) Install Tesseract OCR
- [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)

### 4. Run the app
```bash
streamlit run app.py
```

## ⚡ How It Works
- **Text Input:** Enter text directly into a text area. If it's sufficiently long, the summarizer will condense it into a shorter version.
- **Image Input:** Upload an image. The app will use Tesseract OCR to extract text from the image, then summarize that text.

## 🙌 Acknowledgements
- HuggingFace for the summarization model.
- Tesseract OCR for text extraction.
- Streamlit for making it easy to build data apps.
