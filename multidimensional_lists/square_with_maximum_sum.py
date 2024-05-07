row, col = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]

max_sum = float('-inf')
biggest_square = []

for row_i in range(row - 1):

    for col_i in range(col - 1):
        current_e = matrix[row_i][col_i]
        next_e = matrix[row_i][col_i + 1]
        bottom_e = matrix[row_i + 1][col_i]
        diagonal_e = matrix[row_i + 1][col_i + 1]
        current_square = [[current_e, next_e], [bottom_e, diagonal_e]]

        sum_of_current_square = current_e + next_e + bottom_e + diagonal_e

        if sum_of_current_square > max_sum:
            max_sum = sum_of_current_square
            biggest_square = current_square

print(*biggest_square[0])
print(*biggest_square[1])
print(max_sum)