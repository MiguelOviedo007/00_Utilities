import pyautogui
import time
import sys
import pytesseract
import pyperclip
from PIL import ImageGrab
from pynput.mouse import Listener
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def extract_text_from_image(image):
    try:
        extracted_text = pytesseract.image_to_string(image)
        return extracted_text.strip()
    except Exception as e:
        print("Error during OCR:", e)
        return None

def copy_text_to_clipboard(text):
    try:
        pyperclip.copy(text)
        print("Text copied to clipboard:", text)
    except Exception as e:
        print("Error copying text to clipboard:", e)

def trigger_snipping_tool():
    # Simulate Win+Shift+S keyboard shortcut to trigger the snipping tool
    pyautogui.keyDown('winleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.press('s')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('winleft')
    time.sleep(2)
    
def on_click(x, y, button, pressed):
    global is_clicking
    if pressed:
        print('Clicked!')
        is_clicking = True
    else:
        print('Released!')
        is_clicking = False
        # Interruzione del listener del mouse dopo il rilascio del pulsante
        return False


# Trigger the snipping tool
trigger_snipping_tool()

# Avvio del listener del mouse
with Listener(on_click=on_click) as listener:
    listener.join()
    # Attendi il rilascio del pulsante prima di uscire dal ciclo
    while is_clicking:
        pass

# Introduce a delay to allow time for the snipping tool to capture the screen
time.sleep(1)

# Extract the snipped image from the clipboard
screenshot = ImageGrab.grabclipboard()
if screenshot:
    # Extract text from the snipped image
    extracted_text = extract_text_from_image(screenshot)
    if extracted_text:
        # Copy the extracted text to the clipboard
        copy_text_to_clipboard(extracted_text)
else:
    print("Failed to capture snipped image.")