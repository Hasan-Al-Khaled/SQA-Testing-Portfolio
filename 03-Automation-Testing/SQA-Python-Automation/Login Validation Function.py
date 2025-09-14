def validate_login(user, pwd):
    """Function to validate login credentials"""
    if user == "admin" and pwd == "admin123":
        return "Login Successful"
    elif user == "" or pwd == "":
        return "Empty fields not allowed"
    else:
        return "Invalid credentials"

# Test the function
test_cases = [
    ("admin", "admin123"),
    ("", "admin123"),
    ("admin", ""),
    ("wrong", "wrong")
]

for username, password in test_cases:
    result = validate_login(username, password)
    print(f"Testing {username}/{password}: {result}")