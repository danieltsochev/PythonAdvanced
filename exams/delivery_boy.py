def index_check(f_row, f_col):
    if 0 <= f_row < rows and 0 <= f_col < cols:
        return True
    else:
        return False


rows, cols = [int(x) for x in input().split()]

matrix = []

position = []
start = []

for r in range(rows):
    matrix.append([element for element in input()])
    if "B" in matrix[r]:
        position.append(r)
        position.append(matrix[r].index("B"))
        start.append(r)
        start.append(matrix[r].index("B"))

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

command = input()

while command:

    current_row = position[0] + direction[command][0]
    current_col = position[1] + direction[command][1]

    if not index_check(current_row, current_col):
        print("The delivery is late. Order is canceled.")
        matrix[start[0]][start[1]] = " "
        break
    if matrix[current_row][current_col] == "*":
        command =input()
        continue

    position = [current_row, current_col]

    if matrix[position[0]][position[1]] == "*":
        command = input()
        continue

    elif matrix[position[0]][position[1]] == "-":
        matrix[position[0]][position[1]] = "."

    elif matrix[position[0]][position[1]] == "P":
        matrix[position[0]][position[1]] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[position[0]][position[1]] == "A":
        matrix[position[0]][position[1]] = "P"
        print("Pizza is delivered on time! Next order...")
        matrix[start[0]][start[1]] = "B"
        break

    command = input()

[print(''.join(rw)) for rw in matrix]