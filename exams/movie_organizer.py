def movie_organizer(*movie_data):
    movie_book = {}
    final_book = {}
    final_sort = {}
    result = ''
    for name, genre in movie_data:
        if genre not in movie_book.keys():
            movie_book[genre] = [name]
        else:
            movie_book[genre].append(name)

    final_book = dict(sorted(movie_book.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in final_book.items():
        final_sort[key] = sorted(value)

    for k, v in final_sort.items():
        result += f"\n{k} - {len(v)}"
        for x in v:
            result += f"\n* {x}"
    return result.strip()


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")
))