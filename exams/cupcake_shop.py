from collections import deque


def stock_availability(inventory, *args):
    my_inventory = deque(inventory.copy())
    action = args[0]
    if action == "delivery":
        for stock in args[1:]:
            my_inventory.append(stock)

    elif action == "sell":
        if len(args) > 1:
            if type(args[1]) == int:
                if len(my_inventory) >= args[1]:
                    for i in range(args[1]):
                        my_inventory.popleft()
                else:
                    my_inventory.clear()
            elif type(args[1]) == str:
                if len(args) > 2:
                    for element in args[1:]:
                        while element in my_inventory:
                            my_inventory.remove(element)
                elif len(args) == 2:
                    while args[1] in my_inventory:
                        my_inventory.remove(args[1])
        else:
            if len(my_inventory) > 0:
                my_inventory.popleft()
    return list(my_inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))


