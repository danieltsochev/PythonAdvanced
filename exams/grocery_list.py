def shop_from_grocery_list(budget, my_list, *args):

    purchased = []

    for product, price in args:
        if product in my_list:
            if product not in purchased:
                if price <= budget:
                    budget -= price
                    purchased.append(product)
                    my_list.remove(product)
                else:
                    break
            else:
                continue
        else:
            continue
    if not my_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(my_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))