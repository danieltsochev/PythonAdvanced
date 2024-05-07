ROWS, COLS = [int(x) for x in input().split()]


def index_value(rows, cols):
    if 0 <= rows < ROWS and 0 <= cols < COLS:
        return True


matrix = []

position = []

touched_players = 0
moves = 0

all_other_players = 3

for r in range(ROWS):
    matrix.append([element for element in input().split()])
    if "B" in matrix[r]:
        position.append(r)
        position.append(matrix[r].index("B"))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

while all_other_players > 0:
    command = input()
    if command == "Finish":
        break

    current_row = position[0] + directions[command][0]
    current_col = position[1] + directions[command][1]

    if not index_value(current_row, current_col):
        continue

    if matrix[current_row][current_col] == "O":
        continue

    matrix[position[0]][position[1]] = "-"
    position = [current_row, current_col]

    if matrix[current_row][current_col] == "-":
        moves += 1

    elif matrix[current_row][current_col] == "P":
        touched_players += 1
        moves += 1
        all_other_players -= 1
        matrix[current_row][current_col] = "-"

matrix[position[0]][position[1]] = "B"


print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")