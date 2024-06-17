# AI Uncensored.
Private. Liberated. Nuanced.

<br>

## ⚙️ Usage:
```python
if __name__ == "__main__":
    Client = AIUncensored()
    histories = [{
        "role": "user",
        "content": "you are an expert python geek"
    }]
    question = "How to bypass captcha2"
    print(Client.Chat(question, histories))
```

<br>

## 📚 Functions:
#### `AIUncensored.Chat`
- Requests to origin using query.

<br>

## 📄 Sample Response:
```
Bypassing Captcha2 using Python3 can be done with the help of the PyCaptha2 module. PyCaptcha2 is a simple and powerful module to bypass CAPTCHAs. To use PyCaptcha2, follow these steps:

1. Install the required modules
First, you need to install the required modules by running the following command in your terminal.

pip install pysocks
pip install selenium
pip install pytesseract

2. Download the Tesseract OCR
Since pytesseract needs Tesseract OCR to work, download the latest version of Tesseract from the official website: https://github.com/tesseract-ocr/tesseract

3. Set up pytesseract
Make sure to set the path to the Tesseract executable. Add the following line of code before importing pytesseract:

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Windows
# or
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # Linux

4. Download the browser driver for Selenium
You need to download the appropriate browser driver for Selenium. For example, if you are using Chrome, download the ChromeDriver from this link: https://sites.google.com/a/chromium.org/chromedriver/

5. Import the required modules
Import the required modules for our program:

import os
import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from PIL import Image
import pyautogui
import time

6. Create the main function
Create the main function and write the necessary code to bypass the Captcha2:

def bypass_captcha2():
    # Set Chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-proxy-server")

    # Create the driver
    driver = webdriver.Chrome(options=options)

    # Go to the CAPTCHA URL
    driver.get('<CAPTCHA_URL>')

    # Wait for the CAPTCHA image to appear
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'captchaImage')))

    # Get the CAPTCHA image
    captcha_image = driver.find_element(By.ID, 'captchaImage').get_attribute('src')
    captcha_url = captcha_image.replace('?', '')

    # Save the image
    os.makedirs('captchas', exist_ok=True)
    filename = f'captchas/{int(time.time())}.png'
    response = requests.get(captcha_url)
    with open(filename, 'wb') as f:
        f.write(response.content)

    # Process the image
    captcha_text = process_image(filename)
    driver.quit()
    return captcha_text

def process_image(image_path):
    image = Image.open(image_path)
    captcha_text = pytesseract.image_to_string(image, config='--psm 7 -c tessedit_char_whitelist=0123456789ABCDEF')

    # Check if the CAPTCHA can't be recognized
    if not captcha_text:
        return process_image autofill_captcha(image_path)

    return captcha_text

def autofill_captcha(image_path):
    # Use PyAutoGUI to autofill the CAPTCHA
    captcha_image = pyautogui.Image(image_path)
    captcha_text = pytesseract.image_to_string(captcha_image)
    pyautogui.typewrite(captcha_text)
    return captcha_text

7. Call the function
Finally, call the bypass_captcha2 function:

captcha_text = bypass_captcha2()
print(captcha_text)

Remember to replace `<CAPTCHA_URL>` with the URL of the captcha you want to bypass. This code will open the URL, capture the CAPTCHA image, process the image with Tesseract OCR and PyAutoGUI, and then return the CAPTCHA text to you.

Now, you can use `captcha_text` for your desired operations. In most cases, you can directly use the CAPTCHA text to automate tasks like account registration or forum login.
```
