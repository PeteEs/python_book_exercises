import json

filename = 'fav_number.json'

fav_number_w = input("What is your favorite number?: ")

with open(filename, 'w') as f:
    json.dump(fav_number_w, f)

with open(filename,'r') as f:
    fav_number_r = json.load(f)

print(f"I know your favorite number! It's {fav_number_r}.")