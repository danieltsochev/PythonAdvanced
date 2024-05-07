SIZE = int(input())

matrix = []

position = []

initial_armour = 300
enemy_count = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
win = False
lose = False

for r in range(SIZE):
    matrix.append([element for element in input()])
    if "J" in matrix[r]:
        position.append(r)
        position.append(matrix[r].index("J"))
    if "E" in matrix[r]:
        enemy_count += matrix[r].count("E")


while initial_armour > 0 and enemy_count > 0:

    command = input()

    matrix[position[0]][position[1]] = "-"

    current_row = position[0] + directions[command][0]
    current_col = position[1] + directions[command][1]

    position = [current_row, current_col]

    if matrix[current_row][current_col] == "E":
        if enemy_count > 1:
            initial_armour -= 100
            enemy_count -= 1
        else:
            print("Mission accomplished, you neutralized the aerial threat!")
            win = True
            break
        matrix[current_row][current_col] = "-"

    elif matrix[current_row][current_col] == "R":
        initial_armour = 300
        matrix[current_row][current_col] = "-"

matrix[position[0]][position[1]] = "J"

if initial_armour <= 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates {position}!")

[print(''.join(element)) for element in matrix]