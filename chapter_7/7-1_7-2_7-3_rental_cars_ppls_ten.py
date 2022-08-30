car = input("What kind of rental car would you like?: ")
print(f"Let me see if I can find you a {car}.")


no_of_ppl = input("How many ppl are you your dinner group:s ")
if int(no_of_ppl) > 8:
    print("Please wait a moment for a table.")
else:
    print("Table is ready!")


number = input("Number: ")
if int(number) % 10 == 0:
    print("Multiple of 10.")
else:
    print("Not multiple of 10.")

