def remove_duplicate(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


cities = [
    "Ha Noi",
    "Ho Chi Minh",
    "Nam Dinh",
    "Hue",
    "Nam Dinh",
    "Nam Dinh",
    "Ho Chi Minh",
    "Da Nang",
    "Ho Chi Minh",
    "Ha Noi",
    "Ha Noi"
]
unique_cities = remove_duplicate(cities)
print(unique_cities)
