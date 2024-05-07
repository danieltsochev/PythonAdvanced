def index_check(r, c):
    if 0 <= r < rows and 0 <= c < cols:
        return True


rows, cols = [int(x) for x in input().split(",")]

matrix = []

mouse = []

all_cheese = 0
cheese_eaten = 0
last_position = []

move = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

for r in range(rows):
    matrix.append([element for element in input()])
    if "M" in matrix[r]:
        mouse.append(r)
        mouse.append(matrix[r].index("M"))
    if "C" in matrix[r]:
        all_cheese += matrix[r].count("C")

command = input()

while command != "danger":

    matrix[mouse[0]][mouse[1]] = "*"

    current_row = mouse[0] + move[command][0]
    current_col = mouse[1] + move[command][1]

    if not index_check(current_row, current_col):
        matrix[mouse[0]][mouse[1]] = "M"
        print("No more cheese for tonight!")
        break

    if matrix[current_row][current_col] == "@":
        command = input()
        continue

    mouse = [current_row, current_col]

    if matrix[mouse[0]][mouse[1]] == "C":
        matrix[mouse[0]][mouse[1]] = "*"
        cheese_eaten += 1
        if cheese_eaten >= all_cheese:
            last_position = [mouse[0], mouse[1]]
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[mouse[0]][mouse[1]] = "M"
            break

    elif matrix[mouse[0]][mouse[1]] == "T":
        matrix[mouse[0]][mouse[1]] = "M"
        print("Mouse is trapped!")
        break

    command = input()

else:
    print("Mouse will come back later!")
    matrix[mouse[0]][mouse[1]] = "M"

[print(''.join(x)) for x in matrix]
