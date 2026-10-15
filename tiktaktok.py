def print_board(board):
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("---------")


def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # Columns
    for col in range(3):
        if (
            board[0][col] == board[1][col] == board[2][col]
            and board[0][col] != " "
        ):
            return board[0][col]
    # Diagonals
    if (
        board[0][0] == board[1][1] == board[2][2]
        and board[0][0] != " "
    ):
        return board[0][0]
    if (
        board[0][2] == board[1][1] == board[2][0]
        and board[0][2] != " "
    ):
        return board[0][2]
    return None


def is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("ברוכים הבאים למשחק איקס עיגול!")
    print_board(board)

    while True:
        try:
            move = input(
                f"תור השחקן {current_player}. בחרו שורה ועמודה (1-3), לדוג׳ 1 3: "
            )
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
            if (
                row < 0
                or row > 2
                or col < 0
                or col > 2
                or board[row][col] != " "
            ):
                print("מהלך לא חוקי, נסו שוב.")
                continue
            board[row][col] = current_player
            print_board(board)
            winner = check_winner(board)
            if winner:
                print(f"ניצחון ל-{winner}!")
                break
            if is_full(board):
                print("תיקו!")
                break
            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("קלט לא חוקי, נסו שוב.")


if __name__ == "__main__":
    main()