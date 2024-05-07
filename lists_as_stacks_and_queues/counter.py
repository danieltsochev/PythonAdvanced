from collections import deque

first = deque([10, 15, 20, 30])
second = [3, 6, 10, 13]
symbols = deque(["*", "-", "+", "/"])

total_sum = 0

functions = {

    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else 0
}

while first and second and symbols:
    one = first.popleft()
    two = second.pop()

    total_sum += functions[symbols.popleft()](one, two)

print(total_sum)