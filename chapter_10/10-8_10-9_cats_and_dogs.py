cat_file = 'cats.txt'
dog_file = 'dogs.txt'

try:
    with open(cat_file,'r') as fileobject1:
        cat_str = fileobject1.read()
except FileNotFoundError:
    print(f"Sorry, the file {cat_file} does not exist.")
else:
    print(cat_str)

print("")

try:
    with open(dog_file,'r') as fileobject2:
        dog_str = fileobject2.read()
except FileNotFoundError:
    print(f"Sorry, the file {dog_file} does not exist.")
else:
    print(dog_str)