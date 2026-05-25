# Nesting.
capital = {"Pakistan": "Islamabad",
           "Japan": "Tokyo"}

# Nesting a list in dictionary.
travel_log = {
    "Pakistan": ["Islamabad", "Karachi", "Lahore"],
    "Japan": ["Tokyo", "Hiroshima", "Yokohama"]}

# Nesting Dictionary in a dictionary.
travel_log = {
    "Pakistan": {"cities_visited": ["Islamabad", "Karachi", "Lahore"],"total_visits": 12},
    "Japan": {"cities_visited": ["Tokyo", "Hiroshima", "Yokohama"], "total_visits": 5},
}

# Nesting Disctionary in a List.
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
