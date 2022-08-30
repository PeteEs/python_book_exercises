list_of_ppl = []
list_of_ppl = [
    {
        "first_name":"Andrew",
        "last_name":"Roberts",
        "age":30,
        "city":"Mequon"
    },
    {
        "first_name":"Ann",
        "last_name":"Reds",
        "age":27,
        "city":"Milano"
    }
]

for person in list_of_ppl:
    for key in person.keys():
        print(f"{key} : {person[key]}")
    print("\n")

print(type(list_of_ppl))

# -------------------------------------

pets = [
    {
        "kind" : "dog",
        "name" : "alex",
        "owner" : "andrew"
    },
    {
        "kind" : "cat",
        "name" : "mia",
        "owner" : "ann"
    },
    {
        "kind" : "dog",
        "name" : "mike",
        "owner" : "john"
    }
]

for pet in pets:
    for key, value in pet.items():
        print(f"{key} : {value}")
    print("\n")

