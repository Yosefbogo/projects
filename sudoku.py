board = [

    [1, 5, 3, 6, 2, 8, 0, 0, 0],
    [4, 6, 0, 1, 0, 5, 3, 0, 0],
    [2, 9, 0, 0, 4, 0, 5, 6, 0],
    [8, 3, 0, 0, 6, 0, 0, 0, 0],
    [9, 1, 6, 0, 0, 3, 7, 0, 0],
    [5, 7, 0, 9, 0, 4, 0, 0, 0],
    [6, 2, 0, 5, 0, 0, 0, 0, 4],
    [7, 8, 0, 0, 0, 0, 0, 0, 0],
    [3, 4, 5, 0, 0, 0, 0, 0, 0]

]





def solve(bo):
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num
            print(bo[row])

            if solve(bo):
                return True
            bo[row][col] = 0

    return False



def valid(bo, num, pos):
    row, col = pos

    # check row
    if num in bo[row]:
        return False

    # check col
    for i in range(len(bo)):
        for _ in bo[i]:
            if num == bo[i][col]:
                return False

    # check box
    start = row // 3 * 3
    end = start + 3
    for i in range(start, end):
        start = col // 3 * 3
        end = start + 3
        for j in range(start, end):
            if bo[i][j] == num:
                return False
    return True


def print_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print("- " * 11)

        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print("| ", end="")

            if col == 8:
                print(bo[row][col])
            else:
                print(str(bo[row][col]), end=" ")



def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)





print_board(board)
print("-------------------------")
print("-------------------------")
solve(board)
print_board(board)
