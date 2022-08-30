current_users = ["pepe124","wolf52","johny2545","ann24"]

new_users = ["ann24","wolf52","britt2421","noone231"]



for new_user in new_users:
    print(new_user)
    for curr_user in current_users:
        if new_user in current_users:
            print("Hey! This username is taken!")
            break
        else:
            print("Hi! This username is available")
            break
        