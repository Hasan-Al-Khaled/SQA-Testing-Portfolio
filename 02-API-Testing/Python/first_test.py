# first_test.py
print("🎉 Congratulations! Pycharm is working perfectly!")
print("আমরা এখন Day 9 এর coursework শুরু করতে পারি!")

# Simple test function
def test_addition(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

# Test the function
test_addition(5, 3)
test_addition(10, 7)

# File operations test
import json

test_data = {
    "project": "SQA Learning",
    "day": 9,
    "topics": ["Python", "API Testing", "Postman"]
}

with open("data.json", "w") as file:
    json.dump(test_data, file, indent=4)

print("Data file created successfully!")