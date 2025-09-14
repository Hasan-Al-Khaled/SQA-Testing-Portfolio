from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome with Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Go to Daraz
driver.get("https://www.daraz.com.bd")

# Print page title
print("Page title is:", driver.title)

# Search for mobile
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("mobile")
search_box.submit()

# Print first result text
first_item = driver.find_element(By.CSS_SELECTOR, ".info--ifj7U .title--wFj93")
print("First item found:", first_item.text)

driver.quit()
