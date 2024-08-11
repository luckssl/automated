import webbrowser
import time
import pyautogui
import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd ='C:\Program Files\Tesseract-OCR\Tesseract.exe'

def verificar_dinheiro():
    # Captura a tela na região especificada
    pyautogui.screenshot(region=(751, 230, 70, 33)).save('screenshot.png')
    img = cv2.imread('screenshot.png')
    numero = pytesseract.image_to_string(img)
    numero = numero.replace(',', '').replace(' ', '').strip()
    os.remove('screenshot.png')
    return int(numero)

# Abre o site do jogo
webbrowser.open("https://www.crazygames.com/game/doge-miner-2?_gl=1*b8n7w5*_ga*NDI4MTQ0ODQwLjE3MjMxMzM1NDk.*_ga_37GXT4VGQK*MTcyMzI1MjIwMC41LjEuMTcyMzI1NTAzNC4wLjAuMA..")

time.sleep(10)

# Executa as ações de clique no jogo
pyautogui.moveTo(924, 597)
pyautogui.click()

time.sleep(10)

pyautogui.click()

time.sleep(5)

pyautogui.moveTo(734, 480)


dinheiro = 0

while dinheiro < 50000:
    pyautogui.click()
    dinheiro = verificar_dinheiro()
    print(dinheiro)

# Após atingir o valor desejado, realiza a ação final
pyautogui.moveTo(1296, 480)
pyautogui.click()
pyautogui.moveTo(734, 480)
pyautogui.click()
time.sleep(5)
pyautogui.click()