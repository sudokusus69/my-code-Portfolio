import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "street": '123 Main St',
        "zip": 10001,
        "country": "USA",
        "city": "New York",
        "state": "NY"
    },
    "graduation_years": None
}


x = json.dumps(x, separators=(" ," , "="), indent = 5, sort_keys=True)
print(x)