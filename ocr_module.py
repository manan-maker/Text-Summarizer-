from PIL import Image
import pytesseract

# Windows-specific path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Rudra borda\OneDrive\Desktop'

def extract_text_from_image(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)
