size = int(input())

matrix = []

position = []

money = 100

jackpot_won = False
lines_counter = 0

direct = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append([element for element in input()])
    if "G" in matrix[row]:
        position = [row, matrix[row].index("G")]


while 0 <= position[0] < size and 0 <= position[1] < size:

    command = input()

    lines_counter += 1

    if command == "end":
        break

    if money <= 0:
        break

    matrix[position[0]][position[1]] = "-"

    current_row = position[0] + direct[command][0]
    current_col = position[1] + direct[command][1]
    position = [current_row, current_col]

    if matrix[position[0]][position[1]] == "W":
        money += 100

    elif matrix[position[0]][position[1]] == "P":
        money -= 200

    elif matrix[position[0]][position[1]] == "J":
        money += 100000
        matrix[position[0]][position[1]] = "G"
        jackpot_won = True
        break

    matrix[position[0]][position[1]] = "G"

else:
    print("Game over! You lost everything!")

if money <= 0:
    print("Game over! You lost everything!")

elif money > 0 and not jackpot_won:
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in matrix]
elif money > 0 and jackpot_won:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in matrix]