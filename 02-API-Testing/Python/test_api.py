# api_testing/test_api.py
import requests
import json


def test_jsonplaceholder_api():
    print("Testing JSONPlaceholder API...")

    # GET request to users endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {response.elapsed.total_seconds()} seconds")

    if response.status_code == 200:
        users = response.json()
        print(f"Number of users: {len(users)}")

        # Save response to file - PROPERLY INDENTED
        with open("api_response.json", "w") as file:
            json.dump(users, file, indent=4)
        print("API response saved to api_response.json")

        return True
    else:
        print("API request failed!")
        return False


# Run the test
if __name__ == "__main__":
    test_jsonplaceholder_api()