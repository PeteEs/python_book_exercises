filename = 'guestbook.txt'

while True:
    print("\nPlease enter your name!")
    print("Enter 'q' anytime for quit.")

    first_name = input("First name: ")
    if first_name == 'q':
        break

    last_name = input("Last name: ")
    if last_name == 'q':
        break

    print("And your opinion!")

    opinion = input("Opinion: ")
    if opinion == 'q':
        break

    if first_name != 'q' and last_name != 'q' and opinion != 'q':
        with open(filename,'a') as fileobject:
            fileobject.write(f"{first_name.title()} {last_name.title()}\n")
            fileobject.write(f"Opinion: {opinion}\n")


