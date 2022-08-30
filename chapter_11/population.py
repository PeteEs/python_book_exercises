def city_country_population(city,country,population=None):
    if population:
        concat = f"{city.title()}, {country.title()} - population {population}"
    else:
        concat = f"{city.title()}, {country.title()}"
    return concat
