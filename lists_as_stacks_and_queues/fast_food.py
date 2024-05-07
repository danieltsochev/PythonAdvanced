from collections import deque

orders_queue = deque()

quantity_of_food = int(input())

orders = input().split()

for order in orders:
    orders_queue.append(int(order))

print(max(orders_queue))

for i in range(len(orders_queue)):
    if orders_queue[0] <= quantity_of_food:
        quantity_of_food -= orders_queue[0]
        orders_queue.popleft()

if len(orders_queue) <= 0:
    print("Orders complete")
else:
    left_orders = []
    for order_left in orders_queue:
        left_orders.append(str(order_left))

    print(f"Orders left: {' '.join(left_orders)}")


