import collections


def isValidSudoku(board):
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for row in range(9):
        for column in range(9):
            if board[row][column] == ".":
                continue

            if board[row][column] in rows[row] or \
                board[row][column] in columns[column] or \
                board[row][column] in squares[(row // 3, column // 3)]:
                return False

            rows[row].add(board[row][column])
            columns[column].add(board[row][column])
            squares[(row // 3, column // 3)].add(board[row][column])

    return True


test_cases = [
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]],

    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
]
test_results = [
    True, False
]

for array, expected in zip(test_cases, test_results):
    print(isValidSudoku(array) == expected)