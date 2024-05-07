from collections import deque

SIZE = int(input())


def index_value(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return True


directions = deque([direction for direction in input().split(", ")])

matrix = []

position = []
collected_hazelnuts = 0

for r in range(SIZE):
    matrix.append([element for element in input()])
    if "s" in matrix[r]:
        position.append(r)
        position.append(matrix[r].index("s"))

way = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for index in range(len(directions)):
    current_direction = directions.popleft()

    current_row = position[0] + way[current_direction][0]
    current_col = position[1] + way[current_direction][1]

    if not index_value(current_row,current_col):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
        break

    position = [current_row, current_col]

    if matrix[position[0]][position[1]] == "h":
        collected_hazelnuts += 1
        matrix[position[0]][position[1]] = "*"

        if collected_hazelnuts >= 3:
            print("Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {collected_hazelnuts}")
            break

    elif matrix[position[0]][position[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
        break

else:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {collected_hazelnuts}")