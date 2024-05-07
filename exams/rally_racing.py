SIZE = int(input())


def index_value(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return True


car = input()

kilometers = 0

matrix = []

position = [0, 0]

finished = False

in_tunel = []
out_tunel = []

for r in range(SIZE):
    matrix.append([element for element in input().split()])
    if "T" in matrix[r]:
        in_tunel.append(r)
        in_tunel.append(matrix[r].index("T"))

for i in range(2):
    out_tunel.insert(0, in_tunel.pop())

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

while not finished:

    command = input()
    if command == "End":
        break

    current_row = position[0] + directions[command][0]
    current_col = position[1] + directions[command][1]

    if index_value(current_row, current_col):
        position = [current_row, current_col]
    else:
        continue

    if matrix[position[0]][position[1]] == ".":
        kilometers += 10

    elif matrix[position[0]][position[1]] == "T":
        matrix[position[0]][position[1]] = "."
        if position == in_tunel:
            position = out_tunel
        elif position == out_tunel:
            position = in_tunel
        matrix[position[0]][position[1]] = "."
        kilometers += 30

    elif matrix[position[0]][position[1]] == "F":
        matrix[position[0]][position[1]] = "C"
        kilometers += 10
        print(f"Racing car {car} finished the stage!")
        finished = True

if not finished:
    print(f"Racing car {car} DNF.")
    matrix[position[0]][position[1]] = "C"

print(f"Distance covered {kilometers} km.")

[print(''.join(element)) for element in matrix]
