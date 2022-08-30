def describe_city(city,country = "Poland"):
    print(f"{city} is in {country}.")

describe_city("Cracow")

describe_city("Warsaw")

describe_city("Chicago","USA")

# -------------------------------

def city_country(city,country):
    message = f"{city.title()}, {country.title()}"
    return message

returned = city_country("Chicago","USA")
print(returned)