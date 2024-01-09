import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance
from io import BytesIO
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# 이미지 대비를 높이는 함수
def enhance_image_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    enhanced_im = enhancer.enhance(1.5)  # 대비를 2배로 높임
    return enhanced_im


# 이미지 URL
image_url = "https://gmsports1.cafe24.com/plugin/kcaptcha/kcaptcha_image.php?t=1691673995286"

# 이미지 다운로드
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
enhanced_image = enhance_image_contrast(image)
text = pytesseract.image_to_string(enhanced_image)

print("추출된 텍스트:", text)
