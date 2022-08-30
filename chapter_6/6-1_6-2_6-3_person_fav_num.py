person = {
    "first_name":"Andrew",
    "last_name":"Roberts",
    "age":30,
    "city":"Mequon"
}

print(person)


fav_numbers = {
    "Andrew" : 19,
    "Johny" : 32,
    "Ann" : 244,
    "Ryan" : 77
}

for key in fav_numbers:
    print(f"{key} : {fav_numbers[key]}")


glossary = {
    "bucket" : "a roughly cylindrical open container with a handle, made of metal or plastic and used to hold and carry liquids",
    "wheelbarrow" : "a small cart with a single wheel at the front and two supporting legs and two handles at the rear, used typically for carrying loads in building work or gardening",
    "grout" : "a mortar or paste for filling crevices, especially the gaps between wall or floor tiles"
}