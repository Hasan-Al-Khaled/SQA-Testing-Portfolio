# api_testing/test_with_error_handling.py
import requests
import json


def test_api_with_errors():
    print("Testing API with error handling...")

    try:
        # Test with invalid URL (will fail)
        response = requests.get("https://jsonplaceholder.typicode.com/invalid-endpoint", timeout=5)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("API request successful!")
            return True
        else:
            print(f"API returned error: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"JSON parsing failed: {e}")
        return False


if __name__ == "__main__":
    test_api_with_errors()