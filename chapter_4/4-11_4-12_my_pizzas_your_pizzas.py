my_pizza_list = ["Neapolitan","California","Sicilian","Greek","Pepperoni"]

friend_pizza_list = my_pizza_list[:]

my_pizza_list.append("Capricciosa")

friend_pizza_list.append("Ziti")

print("My favorite pizzas are:")
for pizza in my_pizza_list:
    print(pizza)

print("Friend's favorite pizzas are:")
for pizza in friend_pizza_list:
    print(pizza)