def forecast(*args):

    data = {}

    result = []
    sunny = []
    cloudy = []
    rainy = []

    for city, weather in args:
        data[city] = weather

    data_sort = dict(sorted(data.items()))

    for key, value in data_sort.items():
        if value == "Sunny":
            sunny.append(f"{key} - {value}")
        elif value == "Cloudy":
            cloudy.append(f"{key} - {value}")
        elif value == "Rainy":
            rainy.append(f"{key} - {value}")

    result = sunny + cloudy + rainy

    return '\n'.join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")
))