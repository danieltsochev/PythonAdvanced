from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_foods = deque([int(x) for x in input().split()])

foods = 0

while amount_of_money and prices_foods:

    current_change = amount_of_money.pop()
    current_price = prices_foods.popleft()

    if current_change > current_price:
        foods += 1
        if len(amount_of_money) > 1:
            result = current_change - current_price
            amount_of_money.append(result + amount_of_money.pop())

    elif current_change == current_price:
        foods += 1


if foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")
elif foods == 1:
    print(f"Henry ate: {foods} food.")
elif 1 < foods < 4:
    print(f"Henry ate: {foods} foods.")
else:
    print("Henry remained hungry. He will daniel next weekend again.")