import requests
import time
import pyfiglet
from colorama import init, Fore, Style

init()
text = "Ghost"
formatted_text = pyfiglet.figlet_format(text)
print (Fore.BLUE + formatted_text + Style.RESET_ALL)
words = [Fore.MAGENTA + "<Ghost> : "+ Style.RESET_ALL,"Hi","user","welcome","to",Fore.MAGENTA +"@Ghost"+ Style.RESET_ALL,Fore.RED +":)"+Style.RESET_ALL,Fore.MAGENTA +"\n\n<Ghost> : "+ Style.RESET_ALL,"Ghost", "is",Fore.RED +"simple","virus","and","tools"+ Style.RESET_ALL,"for","Beginner","programming","in","python"]
for word in words:
    print(word, end=' ', flush=True)
    time.sleep(0.09)  
print()  
words = [Fore.MAGENTA + "<Ghost> : "+ Style.RESET_ALL,"https://t.me/ghostchannel3"]
for word in words:
    print(word, end=' ', flush=True)
    time.sleep(0.09)  
print()  
def initialize_board():
    return [' ' for _ in range(9)] 
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]   
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def is_board_full(board):
    return ' ' not in board
def play_game():
    board = initialize_board()
    current_player = 'X' 
    while True:
        print_board(board)        
        move = -1
        while move < 0 or move > 8 or board[move] != ' ':
            try:
                move = int(input(f"Player {current_player}, enter a position (0-8): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
        board[move] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    play_game()
