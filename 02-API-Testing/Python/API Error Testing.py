# api_testing/test_errors.py
import requests


def test_error_scenarios():
    print("Testing API error scenarios...")

    # Test 1: Non-existent endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")
    print(f"Non-existent endpoint: {response.status_code}")

    # Test 2: Invalid user ID
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    print(f"Invalid user ID: {response.status_code}")

    # Test 3: Timeout test
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=0.001)
    except requests.exceptions.Timeout:
        print("Timeout test: Request timed out (as expected)")


if __name__ == "__main__":
    test_error_scenarios()