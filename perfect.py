sum=0
num=int(input("Enter any number : "))
for i in range(1,num):
    if num%i==0:
        sum=i+sum
if sum==num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')




# def print_board(board):
#     print()
#     for i, row in enumerate(board):
#         print(" | ".join(cell if cell != "" else " " for cell in row))
#         if i < 2:
#             print("-" * 9)
#     print()


# def check_win(board, player):
#     for row in board:
#         if all(s == player for s in row):
#             return True
#     for col in range(3):
#         if all(board[row][col] == player for row in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or \
#        all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False


# def is_full(board):
#     return all(cell in ['X', 'O'] for row in board for cell in row)


# def tic_tac_toe():
#     board = [["", "", ""], ["", "", ""], ["", "", ""]]
#     current_player = "X"

#     while True:
#         print_board(board)
#         move = input(f"Player {current_player}, enter your move (1-9): ")

#         if not move.isdigit() or not (1 <= int(move) <= 9):
#             print("Invalid move. Try again.")
#             continue

#         move = int(move)
#         row, col = divmod(move - 1, 3)

#         if board[row][col] in ["X", "O"]:
#             print("Spot already taken. Try again.")
#             continue

#         board[row][col] = current_player

#         if check_win(board, current_player):
#             print_board(board)
#             print(f"Player {current_player} wins!")
#             break

#         if is_full(board):
#             print_board(board)
#             print("It's a tie!")
#             break

#         current_player = "O" if current_player == "X" else "X"


# if __name__ == "__main__":
#     tic_tac_toe()
