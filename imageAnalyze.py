"""
Your module description
"""
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
def image(fileName):
    return (pytesseract.image_to_string(Image.open(fileName)))
