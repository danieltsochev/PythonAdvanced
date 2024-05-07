SIZE = int(input())


def out_of_range(f_row, f_col):
    if 0 <= f_row < SIZE and 0 <= f_col < SIZE:
        return True


matrix = []
position = []

food_quantity = 0
burrows = []
burrow_in = []
burrow_out = []

for r in range(SIZE):
    matrix.append([element for element in input()])
    if "S" in matrix[r]:
        position.append(r)
        position.append(matrix[r].index("S"))
    if "B" in matrix[r]:
        burrows.append(r)
        burrows.append(matrix[r].index("B"))

burrow_in = burrows[0:2]
burrow_out = burrows[2:]

last_r = position[0]
last_c = position[1]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while food_quantity < 10:

    matrix[position[0]][position[1]] = "."

    command = input()

    current_row = position[0] + directions[command][0]
    current_col = position[1] + directions[command][1]

    if not out_of_range(current_row, current_col):
        print("Game over!")
        break

    position = [current_row, current_col]

    if matrix[current_row][current_col] == "*":
        food_quantity += 1
        matrix[current_row][current_col] = "."

    elif matrix[current_row][current_col] == "B":
        if current_row == burrow_in[0] and current_col == burrow_in[1]:
            position = burrow_out
            matrix[current_row][current_col] = "."
        elif current_row == burrow_out[0] and current_col == burrow_out[1]:
            position = burrow_in
            matrix[current_row][current_col] = "."

else:
    print("You won! You fed the snake.")
    matrix[position[0]][position[1]] = "S"

print(f"Food eaten: {food_quantity}")

[print(''.join(element)) for element in matrix]