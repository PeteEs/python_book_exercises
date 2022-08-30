flag = True

while flag == True:
    age = input("Please enter your age: ")
    if age == 'quit':
        flag = False
        #break
    else:
        age = int(age)
        if age < 3:
            print("Ticket is free!")
        elif age <= 12:
            print("Ticket price is $10.")
        else:
            print("Ticket price is $15.")
    
