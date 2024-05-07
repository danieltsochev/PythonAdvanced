size = int(input())

matrix = []

position = []

amount_of_fish = 0

ship_sank = False

direct = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append([element for element in input()])
    if "S" in matrix[row]:
        position = [row, matrix[row].index("S")]

while True:
    command = input()
    if command == "collect the nets":
        break

    matrix[position[0]][position[1]] = "-"

    row_move = direct[command][0] + position[0]
    col_move = direct[command][1] + position[1]



    if row_move < 0:
        row_move = size - 1
    elif row_move >= size:
        row_move = 0

    if col_move < 0:
        col_move = size - 1
    elif col_move >= size:
        col_move = 0

    position = [row_move, col_move]

    if matrix[row_move][col_move].isdigit():
        amount_of_fish += int(matrix[row_move][col_move])

    if matrix[row_move][col_move] == "W":
        ship_sank = True
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last "
              f"coordinates of the ship: {'[' + str(position[0]) + ',' + str(position[1]) + ']'}")
        break

    matrix[row_move][col_move] = "-"
    matrix[position[0]][position[1]] = "S"

if not ship_sank:
    if amount_of_fish >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! "
              f"You need {20 - amount_of_fish} tons of fish more.")

    if amount_of_fish > 0:
        print(f"Amount of fish caught: {amount_of_fish} tons.")

    for row in matrix:
        result = ''
        for element in row:
            result += element
        print(result)
