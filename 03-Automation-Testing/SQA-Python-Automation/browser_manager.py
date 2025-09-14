from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BrowserManager:
    """Manage browser instances"""

    @staticmethod
    def get_chrome_driver():
        """Get Chrome WebDriver instance"""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver

    @staticmethod
    def close_browser(driver):
        """Close browser safely"""
        if driver:
            driver.quit()
            print("Browser closed successfully")