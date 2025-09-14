from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# Maximize window
driver.maximize_window()

# Search box এ টেক্সট লিখবো
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("SQA learning with Python")

# ২ সেকেন্ড wait
time.sleep(2)

# Search button এ Enter চাপবো
search_box.submit()

# ৫ সেকেন্ড পরে ব্রাউজার বন্ধ
time.sleep(5)
driver.quit()
