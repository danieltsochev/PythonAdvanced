def cookbook(*args):
    recipe_book = {}

    for element in args:
        recipe, country, products = element
        if country not in recipe_book:
            recipe_book[country] = []
        recipe_book[country].append(element)

    result = sorted(recipe_book.keys(), key=lambda x: (-len(recipe_book[x]), x))

    result_as_a_string = ""

    for country in result:
        args = recipe_book[country]
        result_as_a_string += f"{country} cuisine contains {len(args)} recipes:\n"
        sorted_recipes = sorted(args, key=lambda x: x[0])
        for element in sorted_recipes:
            recipe_name, _, ingredients = element
            result_as_a_string += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"

    return result_as_a_string.strip()


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))