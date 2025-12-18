import random
from graphics_diana import *

# constanta pentru obstacol
obstacle = -1

# copiere tabla
def copy_board(board):
    # aceasta functie creeaza o copie completa a tablei
    # nu modific tabla originala direct, pentru a evita efecte nedorite

    new_board = []
    r = 0
    size = len(board)

    # parcurgem fiecare rand al tablei
    while r < size:
        new_row = []
        c = 0

        # parcurgem fiecare coloana din randul curent
        while c < size:
            new_row.append(board[r][c])
            c = c + 1

        # adaugam randul copiat in tabla noua
        new_board.append(new_row)
        r = r + 1

    return new_board

# strangere valori
def compress(row):
    # functia muta toate valorile diferite de 0 spre stanga si elimina zerourile dintre ele

    new_row = []
    i = 0

    # parcurgem randul si copiem doar valorile nenule
    while i < len(row):
        if row[i] != 0:
            new_row.append(row[i])
        i = i + 1

    # dupa ce am eliminat zerourile dintre valori, completam randul cu zerouri pana la lungimea initiala
    while len(new_row) < len(row):
        new_row.append(0)

    return new_row

# combinare valori
def merge(row):
    # aceasta functie combina valorile egale alaturate
    # fiecare pereche se combina o singura data pe mutare
    # in acelasi timp calculam scorul obtinut din combinari

    score = 0
    i = 0

    # parcurgem randul pana la penultimul element
    while i < len(row) - 1:
        # verificam daca doua valori vecine sunt egale si diferite de 0, pt a evita combinari nevalide
        if row[i] != 0 and row[i] == row[i + 1]:
            # dublam valoarea din stanga
            row[i] = row[i] * 2

            # adaugam valoarea obtinuta la scor
            score = score + row[i]

            # pozitia din dreapta devine 0
            row[i + 1] = 0
        i = i + 1

    return row, score

# procesare segment
def process_segment(segment):
    # un segment reprezinta valorile dintre doua obstacole
    # pe fiecare segment aplicam aceeasi logica: eliminam zerourile, combinam valorile egale, eliminam din nou zerourile rezultate

    segment = compress(segment)
    segment, score = merge(segment)
    segment = compress(segment)

    return segment, score

# mutare la stanga
def move_left(board):

    size = len(board)
    new_board = []
    total_score = 0

    r = 0
    # parcurgem fiecare rand al tablei
    while r < size:
        result_row = []
        segment = []

        c = 0
        # parcurgem randul de la stanga la dreapta
        while c < size:
            if board[r][c] == obstacle:
                # cand intalnim un obstacol procesam valorile stranse pana in acest punct
                if len(segment) > 0:
                    segment, score = process_segment(segment)
                    total_score = total_score + score

                    i = 0
                    while i < len(segment):
                        result_row.append(segment[i])
                        i = i + 1

                    # resetam segmentul pentru urmatoarele valori
                    segment = []

                # adaugam obstacolul in randul rezultat
                result_row.append(obstacle)
            else:
                # daca nu este obstacol, adaugam valoarea in segmentul curent
                segment.append(board[r][c])

            c = c + 1

        # dupa ce am terminat randul, procesam ultimul segment ramas
        if len(segment) > 0:
            segment, score = process_segment(segment)
            total_score = total_score + score

            i = 0
            while i < len(segment):
                result_row.append(segment[i])
                i = i + 1

        # completam randul cu zerouri pt a pastra dimensiunea corecta a tablei
        while len(result_row) < size:
            result_row.append(0)

        new_board.append(result_row)
        r = r + 1

    return new_board, total_score

# mutare la dreapta
def move_right(board):

    size = len(board)
    new_board = []
    total_score = 0

    r = 0
    while r < size:
        result_row = []
        segment = []

        c = size - 1
        # parcurgem randul de la dreapta la stanga
        while c >= 0:
            if board[r][c] == obstacle:
                if len(segment) > 0:
                    segment, score = process_segment(segment)
                    total_score = total_score + score

                    i = len(segment) - 1
                    while i >= 0:
                        result_row.append(segment[i])
                        i = i - 1

                    segment = []
                result_row.append(obstacle)
            else:
                segment.append(board[r][c])

            c = c - 1

        # procesam ultimul segment ramas
        if len(segment) > 0:
            segment, score = process_segment(segment)
            total_score = total_score + score

            i = len(segment) - 1
            while i >= 0:
                result_row.append(segment[i])
                i = i - 1

        # completam randul cu zerouri
        while len(result_row) < size:
            result_row.append(0)

        # inversam randul rezultat
        final_row = []
        i = len(result_row) - 1
        while i >= 0:
            final_row.append(result_row[i])
            i = i - 1

        new_board.append(final_row)
        r = r + 1

    return new_board, total_score

# mutare sus
def move_up(board):
    # am ales sa lucrez pe coloane in loc de randuri pt ca mutarea in sus inseamna deplasarea valorilor
    # de jos in sus pe fiecare coloana

    size = len(board)
    new_board = [[0] * size for _ in range(size)]
    total_score = 0

    c = 0
    # parcurgem fiecare coloana
    while c < size:
        segment = []
        result_col = []

        r = 0
        # parcurgem coloana de sus in jos
        while r < size:
            if board[r][c] == obstacle:
                if len(segment) > 0:
                    segment, score = process_segment(segment)
                    total_score = total_score + score

                    i = 0
                    while i < len(segment):
                        result_col.append(segment[i])
                        i = i + 1

                    segment = []
                result_col.append(obstacle)
            else:
                segment.append(board[r][c])

            r = r + 1

        # procesam ultimul segment ramas
        if len(segment) > 0:
            segment, score = process_segment(segment)
            total_score = total_score + score

            i = 0
            while i < len(segment):
                result_col.append(segment[i])
                i = i + 1

        # completam coloana cu zerouri
        while len(result_col) < size:
            result_col.append(0)

        # copiem coloana rezultata in tabla noua
        r = 0
        while r < size:
            new_board[r][c] = result_col[r]
            r = r + 1

        c = c + 1

    return new_board, total_score

# mutare jos
def move_down(board):
    # am ales sa parcurg coloanele de jos in sus
    # pentru a respecta directia mutarii
    # logica este similara cu move_up, dar inversata

    size = len(board)
    new_board = [[0] * size for _ in range(size)]
    total_score = 0

    c = 0
    while c < size:
        segment = []
        result_col = []

        r = size - 1
        # parcurgem coloana de jos in sus
        while r >= 0:
            if board[r][c] == obstacle:
                if len(segment) > 0:
                    segment, score = process_segment(segment)
                    total_score = total_score + score

                    i = len(segment) - 1
                    while i >= 0:
                        result_col.append(segment[i])
                        i = i - 1

                    segment = []
                result_col.append(obstacle)
            else:
                segment.append(board[r][c])

            r = r - 1

        # procesam ultimul segment ramas
        if len(segment) > 0:
            segment, score = process_segment(segment)
            total_score = total_score + score

            i = len(segment) - 1
            while i >= 0:
                result_col.append(segment[i])
                i = i - 1

        # completam coloana cu zerouri
        while len(result_col) < size:
            result_col.append(0)

        # copiem coloana rezultata in tabla noua
        r = 0
        while r < size:
            new_board[size - 1 - r][c] = result_col[r]
            r = r + 1

        c = c + 1

    return new_board, total_score

# verificare schimbare tabla
def board_changed(old_board, new_board):
    # aceasta functie verifica daca tabla s a modificat
    # este folosita pentru a decide daca mutarea este valida
    # am ales aceasta verificare pentru a evita mutari inutile

    if old_board != new_board:
        return True
    else:
        return False

# adaugare obstacole
def add_obstacles(board, count):
    # aceasta functie adauga un numar de obstacole pe tabla
    # am ales sa primesc ca parametri tabla si numarul de obstacole
    # pentru a putea controla usor cate obstacole apar in joc

    size = len(board)
    empty_cells = []

    # parcurgem intreaga tabla
    # si memoram toate pozitiile care sunt libere (valoarea 0)
    r = 0
    while r < size:
        c = 0
        while c < size:
            if board[r][c] == 0:
                empty_cells.append((r, c))
            c = c + 1
        r = r + 1

    # daca numarul de obstacole cerut este mai mare
    # decat numarul de celule libere disponibile
    # il limitam pentru a evita erori
    if count > len(empty_cells):
        count = len(empty_cells)

    # alegem aleator pozitii libere pentru obstacole
    # am ales random.sample pentru ca returneaza pozitii diferite fara a repeta aceeasi pozitie
    positions = random.sample(empty_cells, count)

    # plasam obstacolele pe pozitiile alese
    # modificam direct tabla primita ca parametru
    i = 0
    while i < len(positions):
        r = positions[i][0]
        c = positions[i][1]
        board[r][c] = obstacle
        i = i + 1

    return board

# verificare daca mai exista mutari posibile

def any_moves_possible(board):

    # jocul continua daca exista cel putin o mutare valida

    size = len(board)

    # verificam daca exista celule libere
    # daca exista macar un 0 pe tabla
    # inseamna ca se poate face cel putin o mutare
    # deoarece o valoare poate fi mutata in acel loc
    r = 0
    while r < size:
        c = 0
        while c < size:
            if board[r][c] == 0:
                return True
            c = c + 1
        r = r + 1

    # verificare orizontala
    # daca doua valori egale sunt alaturate pe acelasi rand
    # si nu sunt separate de un obstacol
    # atunci ele se pot combina intr-o mutare
    r = 0
    while r < size:
        c = 0
        while c < size - 1:
            if board[r][c] != obstacle and board[r][c] == board[r][c + 1]:
                return True
            c = c + 1
        r = r + 1

    # verificare verticala
    # aceeasi logica este aplicata si pe coloane
    # daca doua valori egale sunt una sub alta
    # si nu exista obstacol intre ele
    # atunci jocul poate continua
    c = 0
    while c < size:
        r = 0
        while r < size - 1:
            if board[r][c] != obstacle and board[r][c] == board[r + 1][c]:
                return True
            r = r + 1
        c = c + 1

    # daca nu exista celule libere si nu exista valori egale alaturate
    # atunci nu mai exista mutari posibile
    # jocul se termina
    return False


# functie generala de mutare
def move_board(board, direction):
    # aceasta functie primeste directia sub forma de string
    # copiem tabla initiala pentru a nu o modifica direct
    # apoi aplicam mutarea pe copia tablei

    board_copy = copy_board(board)
    score = 0

    if direction == "LEFT":
        new_board, score = move_left(board_copy)
    elif direction == "RIGHT":
        new_board, score = move_right(board_copy)
    elif direction == "UP":
        new_board, score = move_up(board_copy)
    elif direction == "DOWN":
        new_board, score = move_down(board_copy)
    else:
        # tratam cazul unei directii invalide
        print("directie invalida")
        return board, 0, False

    # verificam daca tabla s a modificat
    if board_changed(board, new_board):
        return new_board, score, True
    else:
        return board, 0, False

# logica obstacole

# determinare numar obstacole in functie de dimensiune si dificultate
def get_obstacle_count(board_size, difficulty):
    # stabileste cate obstacole vor fi adaugate pe tabla

    if difficulty == "easy":
        if board_size == 4:
            return 2
        if board_size == 5:
            return 3
        if board_size == 6:
            return 4
    else:
        if board_size == 4:
            return 4
        if board_size == 5:
            return 6
        if board_size == 6:
            return 8
    # valoare de siguranta
    return 0

# logica mutari limitate
def get_moves_by_difficulty(difficulty):
    # aceasta functie returneaza numarul de mutari in functie de dificultatea aleasa

    if difficulty == "easy":
        return 250

    if difficulty == "medium":
        return 180

    if difficulty == "hard":
        return 120

    # valoare de siguranta
    return 0
