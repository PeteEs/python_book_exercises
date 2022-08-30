list_of_nums = list(range(1,10))

print(list_of_nums)

for num in list_of_nums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")