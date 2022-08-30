print("Please enter your name!")
first_name = input("First name: ")
last_name = input("Last name: ")

filename = 'guest.txt'

with open(filename,'w') as file_object:
    file_object.write(f"{first_name.title()} {last_name.title()}")