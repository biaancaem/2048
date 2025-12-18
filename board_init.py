import random
from moves_logic import add_obstacles
from graphics_diana import *
obstacle = -1


# initializare tabla goala
def create_empty_board(size):
    # aceasta functie creeaza o tabla patrata de dimensiune size x size
    # toate valorile sunt initializate cu 0

    board = []
    r = 0

    # parcurgem fiecare rand
    while r < size:
        row = []
        c = 0

        # parcurgem fiecare coloana din rand
        while c < size:
            # adaugam valoarea 0 in fiecare celula
            # 0 inseamna celula libera
            row.append(0)
            c = c + 1

        # adaugam randul in tabla
        board.append(row)
        r = r + 1

    return board

# verificare daca tabla este valida
def is_board_valid(board):
    
    # am ales sa fac aceasta verificare pentru siguranta
    # si pentru a evita situatii in care jocul se comporta gresit

    # verificam daca tabla exista

    if board is None:
        return False

    # verificam daca tabla este o matrice patratica
    size = len(board)

    # daca tabla nu are niciun rand
    # nu este o tabla valida
    if size == 0:
        return False

    r = 0
    while r < size:
        # fiecare rand trebuie sa aiba exact size coloane
        if len(board[r]) != size:
            return False
        r = r + 1

    # verificam valorile din tabla
    # valorile permise sunt: 0 (celula libera), obstacle, puteri ale lui 2
    r = 0
    while r < size:
        c = 0
        while c < size:
            value = board[r][c]

            # verificam cazul valorilor speciale
            if value == 0 or value == obstacle:
                c = c + 1
                continue

            # verificam daca valoarea este o putere a lui 2

            if value < 0:
                return False

            temp = value
            while temp > 1:
                if temp % 2 != 0:
                    return False
                temp = temp // 2

            c = c + 1
        r = r + 1
        
    return True

# adaugare numar random pe tabla
def add_nr_random(board):
    # numarul este 2 sau 4
    # alegem o celula libera in mod aleator

    size = len(board)
    empty_cells = []

    r = 0
    # parcurgem toata tabla pentru a gasi celulele libere
    while r < size:
        c = 0
        while c < size:
            if board[r][c] == 0:
                empty_cells.append((r, c))
            c = c + 1
        r = r + 1

    # daca nu exista celule libere
    # nu mai putem adauga un numar nou
    if len(empty_cells) == 0:
        return board

    # alegem aleator o celula libera
    # random.choice returneaza un tuplu (linie, coloana)
    position = random.choice(empty_cells)
    r = position[0]
    c = position[1]

    # generam un numar intre 1 si 10
    # daca numarul este 1, punem valoarea 4 (10% sanse)
    # altfel punem valoarea 2 (90% sanse)
    chance = random.randint(1, 10)
    if chance == 1:
        board[r][c] = 4
    else:
        board[r][c] = 2

    # returnam tabla modificata
    return board

# initializare joc
def init_game(board_size, obstacle_mode=False, obstacle_count=0):

    # cream tabla goala
    board = create_empty_board(board_size)
    if not is_board_valid(board):
        print("eroare: tabla goala invalida")
        return board, 0, 0, True

    # adaugam doua valori initiale pe tabla
    board = add_nr_random(board)
    board = add_nr_random(board)
    if not is_board_valid(board):
        print("eroare: tabla invalida dupa adaugare numere initiale")
        return board, 0, 0, True

    # daca modul cu obstacole este activ
    # si numarul de obstacole este mai mare decat 0
    # adaugam obstacolele pe tabla
    if obstacle_mode and obstacle_count > 0:
        board = add_obstacles(board, obstacle_count)
        
        if not is_board_valid(board):
            print("eroare: tabla invalida dupa adaugare obstacole")
            return board, 0, 0, True

    # initializam scorul cu 0
    score = 0

    # jocul nu este terminat la inceput
    game_over = False

    # best score incepe de la 0
    # va fi actualizat pe parcursul jocului
    best_score = 0

    # returnam toate valorile necesare pentru joc
    return board, score, best_score, game_over
