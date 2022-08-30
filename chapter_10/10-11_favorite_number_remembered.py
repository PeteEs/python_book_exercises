import json

filename = 'fav_number.json'

try:
    with open(filename) as f:
        fav_number = json.load(f)
except FileNotFoundError:
    fav_number = input("What is your favorite number?: ")
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
        print(f"Number {fav_number} saved!")   
else:
    print(f"Stored favorite number: {fav_number}.")