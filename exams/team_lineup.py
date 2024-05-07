def team_lineup(*args):
    data = {}
    result = ''

    for current_tuple in args:
        name, country = current_tuple[0], current_tuple[1]
        if country not in data.keys():
            data[country] = [name]
        else:
            data[country].append(name)
    data_sorting = dict(sorted(data.items(), key=lambda x: (-len(x[1]), x[0])))

    for key, value in data_sorting.items():
        result += f"{key}:\n"
        for v in value:
            result += f"  -{v}\n"
    return result.strip()


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
     ("Toni Kroos", "Germany"),   ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")
))