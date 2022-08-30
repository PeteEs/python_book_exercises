def make_sandwich(*args):
    print("We are preparing sandwich for you.")
    print("Ingredients: ")
    for arg in args:
        print(arg)

make_sandwich("cheese","bread","tomatoe","ham")

make_sandwich("cheese","bread","tomatoe")

make_sandwich("cheese","bread","tomatoe","ham","butter")
