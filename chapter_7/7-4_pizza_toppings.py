print("Please enter a series of pizza toppings.")
print("If you want to finish, enter 'quit'")

prompt = ''
while prompt != 'quit':
    prompt = input("")
    if prompt != 'quit':
        print(f"{prompt} added!")
