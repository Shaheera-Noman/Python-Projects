travel_log = [
    {"country": "Pakistan",
     "cities_visited": ["Islamabad", "Karachi", "Lahore"],
     "total_visits": 12
     },
    {
    "country": "Japan",
    "cities_visited": ["Tokyo", "Hiroshima", "Yokohama"],
    "total_visits": 5}, 
]
def add_new_country(country, cities, times_visits):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities
    new_country["total_visits"] = times_visits

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



