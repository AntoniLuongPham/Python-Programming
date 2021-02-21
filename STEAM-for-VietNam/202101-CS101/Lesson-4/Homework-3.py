def count_frequency(items):
    result = {}
    for item in items:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
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
cities_frequencies = count_frequency(cities)
print(cities_frequencies)
