SIZE = 6


def create(func_command):
    split_command = func_command.split(', ')
    action, direction, value = split_command[0], split_command[1], split_command[2]

    row = first_position[0] + directions[direction][0]
    col = first_position[1] + directions[direction][1]

    if matrix[row][col] == ".":
        matrix[row][col] = value

    return [row, col]


def update(func_command):
    split_command = func_command.split(', ')
    action, direction, value = split_command[0], split_command[1], split_command[2]

    row = first_position[0] + directions[direction][0]
    col = first_position[1] + directions[direction][1]

    if matrix[row][col] != ".":
        matrix[row][col] = value

    return [row, col]


def delete(func_command):
    split_command = func_command.split(', ')
    action, direction = split_command[0], split_command[1]

    row = first_position[0] + directions[direction][0]
    col = first_position[1] + directions[direction][1]

    if matrix[row][col] != ".":
        matrix[row][col] = "."

    return [row, col]


def read(func_command):
    split_command = func_command.split(', ')
    split_command = func_command.split(', ')
    action, direction = split_command[0], split_command[1]

    row = first_position[0] + directions[direction][0]
    col = first_position[1] + directions[direction][1]

    if matrix[row][col] != ".":
        print(matrix[row][col])

    return [row, col]


matrix = [[x for x in input().split()] for i in range(SIZE)]

first_position_as_string = input()

first_position = [int(x) for x in first_position_as_string if x.isdigit()]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == "Stop":
        break

    elif command.startswith("Create"):
        first_position = create(command)

    elif command.startswith("Update"):
        first_position = update(command)

    elif command.startswith("Delete"):
        first_position = delete(command)

    elif command.startswith("Read"):
        first_position = read(command)

[print(' '.join(x)) for x in matrix]