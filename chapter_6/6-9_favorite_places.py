favorite_places = {}

favorite_places = {
    "Ann" : {"Roma","Berlin","Warsaw"},
    "Robert" : {"Barcelona","Athens","Palermo"}
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(place)