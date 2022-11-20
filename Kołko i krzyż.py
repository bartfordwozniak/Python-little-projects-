


#stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instrukt():
    print(
        """
\tWitaj w ble ble kółko i krzyżyk
\t  0 | 1 | 2 |
\t  -----------
\t  3 | 4 | 5 |
\t  -----------
\t  6 | 7 | 8 |
\t
""")

def ask_yes_no(question):
    """Pytanie tak/nie"""
    response = None
    while response not in ("t","n"):
        response = int(input(question))
    return response

def pieces():
    """Ustal, kto 1. ruch"""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu?")
    if go_first == "t":
        print("Zaczynasz")
        human = X
        computer = O
    else:
        print("Zaczynam")
        cumputer = X
        human = O
    return computer, human

def ask_number(question, low, high):
    """Nadanie liczby z zakresu"""
    response = None
    while response not in range(low, high):
        response = int( input(" question" ))
    return response

def new_board():
    """utwórz nową planszę"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\n\t", board [0], "|", board[1], "|", board [2])
    print("----------------")
    print("\t", board [3], "|", board[4], "|", board [5])
    print("----------------")
    print("\t", board [6], "|", board[7], "|", board [8])

def legal_move():
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """drogi zwyciestw"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_numer("Jaki ruch zrobisz? (0-8)", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest zajęte")
    return move


def computer_move(board, computer, human):
    board = board[:]  #kopia robocza
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5 , 7)
    print("Wybieram ", end = " ")

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return(move)
        board[move] = EMPTY

    for move in legal_moves(board):
        print(move)
        return move

def next_turn():
    if trun == X:
        return 0
    else:
        return X

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "jest zwuciezcą\n")
    else:
        print("Remis")

    if the_winner == computer:
        print("Ziemniak, śmierdzisz nie urosłeś!")

    elif the_winner == human:
        print("Zwycięztwo jest Twoje\n")

    elif the_winner == TIE:
        print("REMIS\n")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = computer
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# START progamu

main()
input("\nEnter aby zakończyć")



    






    



    
    

    
    
