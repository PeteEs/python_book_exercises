sandwich_orders = []

sandwich_orders = ["hotdog","fatpig","pastrami","baconed","chickened","pastrami"]

finished_sandwiches = []

print("Deli has run out of pastrami!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f"I made you {order} sandwich.")
    finished_sandwiches.append(order)

print("Sandwiches made:")
for f_sandwich in finished_sandwiches:
    print(f_sandwich)