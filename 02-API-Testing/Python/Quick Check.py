# test_selenium_setup.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_selenium_working():
    print("🚀 Testing Selenium Setup...")

    # Automatic driver setup
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        # Open website
        driver.get("https://www.google.com")
        print("✅ Google opened successfully")

        # Check title
        title = driver.title
        print(f"✅ Page title: {title}")

        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("SQA Testing")
        print("✅ Search box found and text entered")

        time.sleep(2)  # Just to see the result

        print("🎉 All tests passed! Selenium is working perfectly!")

    finally:
        driver.quit()
        print("✅ Browser closed properly")


if __name__ == "__main__":
    test_selenium_working()