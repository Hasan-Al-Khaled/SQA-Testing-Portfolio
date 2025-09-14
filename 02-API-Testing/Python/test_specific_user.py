# api_testing/test_specific_user.py
import requests
import json


def test_specific_user():
    print("Testing specific user API...")

    # Get user with ID 1
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        user = response.json()
        print(f"User Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")

        # Save to file
        with open("user_1.json", "w") as file:
            json.dump(user, file, indent=4)
        print("User data saved to user_1.json")

        return True
    else:
        print("API request failed!")
        return False


if __name__ == "__main__":
    test_specific_user()