class LoginPage:
    """Page Object for Login Page"""

    def __init__(self):
        self.url = "https://demo.opencart.com/login"
        self.email_field = "#input-email"
        self.password_field = "#input-password"
        self.login_button = "input[value='Login']"

    def navigate_to_login(self):
        """Navigate to login page"""
        print(f"Navigating to {self.url}")

    def enter_credentials(self, username, password):
        """Enter login credentials"""
        print(f"Entering username: {username}")
        print(f"Entering password: {'*' * len(password)}")

    def click_login(self):
        """Click login button"""
        print("Clicking login button")
        return "HomePage"  # Simulate returning to home page

    def login(self, username, password):
        """Complete login process"""
        self.navigate_to_login()
        self.enter_credentials(username, password)
        return self.click_login()


# Test the page object
login_page = LoginPage()
result = login_page.login("demo", "demo123")
print(f"Login result: {result}")