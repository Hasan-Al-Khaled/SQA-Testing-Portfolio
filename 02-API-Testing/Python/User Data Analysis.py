# api_testing/analyze_users.py
import requests
import json


def analyze_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    print("=== User Analysis Report ===")
    print(f"Total Users: {len(users)}")

    # Count users per city
    city_count = {}
    for user in users:
        city = user['address']['city']
        city_count[city] = city_count.get(city, 0) + 1

    print("\nUsers by City:")
    for city, count in city_count.items():
        print(f"{city}: {count} users")

    # Find user with website
    print("\nUsers with websites:")
    for user in users:
        if user['website']:
            print(f"{user['name']}: {user['website']}")


if __name__ == "__main__":
    analyze_users()