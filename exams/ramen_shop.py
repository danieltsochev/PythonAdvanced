from collections import deque

bows_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bows_ramen and customers:
    current_bow = bows_ramen.pop()
    current_customer = customers.popleft()

    if current_bow > current_customer:
        bows_ramen.append(current_bow - current_customer)

    elif current_customer > current_bow:
        customers.appendleft(current_customer - current_bow)

if not customers:
    print("Great job! You served all the customers.")
    if bows_ramen:
        print(f"Bowls of ramen left: {', '.join([str(el) for el in bows_ramen])}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")