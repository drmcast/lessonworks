X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9
def display_instruct():
	#Инструкция для игрока
	print("""Чтобы сделать ход, введи число от0 до 8. 
Числа соответствуют полям доски - так, как показано ниже:

0 | 1 | 2
_________
3 | 4 | 5
_________
6 | 7 |	8 \n   """)

def ask_yes_wno(question):
	#Задает вопрос с ответом 'Да' или 'Нет'.
	response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
	#Просит ввести число из диапазона.
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response	

def pieces():
	#Определяет принадлежность первого хода.
	go_first = ask_yes_no("Хочешь оставить за собой первый ход?(y/n): ")
	if go_first == "y":
		print("\nТы играешь крестиками.")
		human = X 
		computer = O 
	else:
		print("\nТы играешь нуликами.")
		computer = X   
		human = O
		return computer.human

def new_board():
#Создает новую игровую доску.
board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board		

def display_board():
#Отображает игровую доску на экране
print('   |   |')
print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
print('   |   |')


def legal_moves(board):
    #Cписок доступных ходов.
    moves = []
for square in range(NUM_SQUARES):
    if board[square] == ЕМРТУ:
        moves.append(square)
return moves

def winner(board):
#Определяет победителя в игре.
ways_to_win = ((0, 1, 2),
               (3, 4, 5),
               (6, 7, 8),
               (0, 3, 6),
               (1, 4, 7),
               (2, 5, 8),
               (0, 4, 8),
               (2, 4, 6))
for row in ways_to_win:
	if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
		winner = board[row[0]]
		return winner
	if EMPTY not in board:
	    return TIE
	    return None

def human_move(board, human):
    #Получает ход игрока.
    legal = legal_moves(board)
    move = None
    while move not in legal:
           move = ask_number("Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in lega1:
           print("Это поле уже занято.\n")
    return move	    
			


