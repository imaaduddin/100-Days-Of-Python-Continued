# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary 

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log_two = {
    "France": {
        "value": ["Paris", "Lille", "Dijon"],
        "cities_visited": 3
    },
    "Germany": ["berlin", "Hamburg", "Stuttgart"],
}