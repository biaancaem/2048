import pygame
import json
import os
import sys
from graphics import *
from graphics_diana import *

from obstacole_options import (
    choose_obstacle_mode,
    choose_obstacle_difficulty,
    get_obstacle_count,
    choose_moves_mode,
    choose_moves_difficulty
)
from board_init import init_game


SAVE_FILE = "savegame.json"


def save_game(state):
    """Salveaza starea completa a jocului intr-un JSON."""
    try:
        # Deschidem fisierul de salvare in modul "write"
        # Daca fisierul nu exista, va fi creat automat
        f = open(SAVE_FILE, "w")

        # Scriem dictionarul 'state' in fisier, sub forma JSON
        json.dump(state, f)

        # Inchidem fisierul dupa scriere
        f.close()
    except:
        # Daca apare orice eroare (ex: nu avem drept de scriere),
        # nu oprim jocul
        pass


def load_game():
    """Incarca jocul daca exista salvare."""

    # Verificam daca fisierul de salvare exista
    if not os.path.exists(SAVE_FILE):
        # Daca nu exista, inseamna ca nu avem joc salvat
        return None
    try:
        # Deschidem fisierul in modul "read"
        f = open(SAVE_FILE, "r")

        # Citim continutul fisierului si il transformam inapoi
        # in dictionar(pereche cheie valoare)
        state = json.load(f)

        # Inchidem fisierul dupa citire
        f.close()

        # Returnam starea jocului
        return state
    except:
        # Daca apare o eroare
        return None


def load_best_score(filename):
    """Incarca best score din JSON."""

    # Verificam daca fisierul exista
    if not os.path.exists(filename):
        return 0 # nu avem best score salvat
    
    try:
        # Deschidem fisierul pentru citire
        f = open(filename, "r")

        # Citim continutul JSON din fisier
        data = json.load(f)

        # Inchidem fisierul
        f.close()

        # Daca exista cheia "best", o returnam
        if "best" in data:
            return data["best"]
        else:
            return 0
    except:
        # Daca apare orice eroare, nu oprim jocul
        return 0
    

def save_best_score(filename, score):
    """Salveaza best score în JSON."""
    try:
        # Deschidem fisierul pentru scriere
        f = open(filename, "w")

        # Cream un dictionar cu best score
        data = {"best": score}

        # Scriem dictionarul in fisier sub forma JSON
        json.dump(data, f)

        # Inchidem fisierul
        f.close()

    except:
        # Daca apare o eroare, nu facem nimic
        pass


def get_board_difficulty(board_size):
    # Stabilim dificultatea in functie de dimensiunea tablei
    if board_size == 4:
        return "hard"
    if board_size == 5:
        return "medium"
    return "easy"


def get_best_score_filename(board_size, timed_mode, obstacle_mode,
                            difficulty_obstacles, moves_difficulty):
    """
    Construieste numele fisierului JSON pentru best score
    in functie de modul de joc ales.
    """

    # Dificultatea tablei (hard / medium / easy)
    board_difficulty = get_board_difficulty(board_size)

    # Incepem construirea numelui fisierului cu dimensiunea tablei
    name = "best_" + str(board_size) + "x" + str(board_size)
    name += "_" + board_difficulty

    # Adaugam daca jocul este cu timp sau nu
    if timed_mode:
        name += "_timed"
    else:
        name += "_normal"

    # Adaugam daca exista obstacole
    if obstacle_mode:
        name += "_obst"
    else:
        name += "_noobst"

    # Adaugam dificultatea obstacolelor
    name += "_" + difficulty_obstacles

    # Adaugam informatia despre mutari
    if moves_difficulty is not None:
        name += "_moves" + str(moves_difficulty)
    else:
        name += "_movesNone"

    # Extensia fisierului
    name += ".json"

    return name


def ask_continue_screen(screen):
    """Intreaba daca utilizatorul vrea sa continue jocul salvat."""

    # Incercam sa incarcam un joc salvat
    saved_game = load_game()

    # Daca nu exista fisier de salvare, nu avem ce continua
    if saved_game is None:
        return None

    # Font folosit pentru text
    font = pygame.font.SysFont("arial", 32)

    # Dimensiunea ferestrei
    width = screen.get_width()
    height = screen.get_height()

    # Bucla care tine ecranul deschis pana apasam o tasta valida
    while True:
        for event in pygame.event.get():

            # Daca utilizatorul inchide fereastra
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Daca apasam o tasta
            if event.type == pygame.KEYDOWN:

                # Y = continua jocul salvat
                if event.key == pygame.K_y:
                    return saved_game

                # N = nu continuam, pornim joc nou
                if event.key == pygame.K_n:
                    return None

        # Fundal simplu
        screen.fill((200, 190, 180))

        # Textele afisate pe ecran
        text1 = font.render("Continue last game?", True, TEXT_COLOR_DARK)
        text2 = font.render("[Y] Yes   |   [N] No", True, TEXT_COLOR_DARK)

        # Pozitionare text pe centru
        screen.blit(text1, (width // 2 - text1.get_width() // 2,
                             height // 2 - 50))
        screen.blit(text2, (width // 2 - text2.get_width() // 2,
                             height // 2 + 10))

        # Actualizam ecranul
        pygame.display.flip()


def start_new_game(start_screen):
    """Incepe un joc nou"""

    # alegem dimensiunea tablei
    board_size = show_start_screen(start_screen)

    # alegem daca jocul este cu timp sau nu
    timed_mode = choose_time_mode(start_screen)

    # alegem daca jocul are obstacole
    obstacle_mode = choose_obstacle_mode(start_screen)

    # valori initiale
    difficulty = "none"
    obstacle_count = 0

    # daca avem obstacole, alegem dificultatea si numarul lor
    if obstacle_mode:
        difficulty = choose_obstacle_difficulty(start_screen)
        obstacle_count = get_obstacle_count(board_size, difficulty)

    # alegem daca avem mutari limitate
    moves_mode = choose_moves_mode(start_screen)

    if moves_mode == "choose":
        moves_left = choose_moves_difficulty(start_screen)
    else:
        moves_left = None  # mutari nelimitate

    # initializam jocul (tabla + scor)
    board, score, best_score, game_over = init_game(
        board_size, obstacle_mode, obstacle_count
    )

    # stive pentru undo / redo
    undo_stack = []
    redo_stack = []

    # stari de joc
    has_won = False
    win_screen_active = False

    # timp de start pentru timer
    start_ticks = pygame.time.get_ticks()

    # calculam dimensiunea ferestrei
    width, height = dimensiune_fereastra(board_size)

    # cream fereastra jocului
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("2048 - Tabla " + str(board_size) + "x" + str(board_size))

    # returnam toate valorile necesare
    return (screen, board, board_size,
            score, best_score, game_over,
            timed_mode, obstacle_mode,
            difficulty, moves_left,
            undo_stack, redo_stack, has_won,
            win_screen_active, start_ticks)


def load_saved_game_and_setup(saved):
    # luam tabla de joc din dictionarul salvat
    board = saved["board"]

    # luam scorul curent din salvare
    score = saved["score"]

    # luam best score-ul din salvare
    best_score = saved["best_score"]

    # luam numarul de mutari ramase (None daca nu exista)
    moves_left = saved["moves_left"]

    # luam daca jocul este in mod cu timp
    timed_mode = saved["timed_mode"]

    # luam timpul ramas din salvare
    remaining_time = saved["remaining_time"]

    # luam daca jocul are obstacole
    obstacle_mode = saved["obstacle_mode"]

    # luam dificultatea obstacolelor
    difficulty_obstacles = saved["difficulty_obstacles"]

    # luam stiva pentru undo
    undo_stack = saved["undo_stack"]

    # luam stiva pentru redo
    redo_stack = saved["redo_stack"]

    # luam daca jucatorul a castigat
    # daca nu exista in salvare, folosim False
    has_won = saved.get("has_won", False)

    # luam daca ecranul de win este activ
    # daca nu exista in salvare, folosim False
    win_screen_active = saved.get("win_screen_active", False)

    # dimensiunea tablei este numarul de linii
    board_size = len(board)

    # calculam dimensiunea ferestrei in functie de tabla
    width, height = dimensiune_fereastra(board_size)

    # recream fereastra jocului
    screen = pygame.display.set_mode((width, height))

    # fortam jocul sa nu fie game over la incarcare
    game_over = False

    # refacem cronometrul astfel incat timpul ramas sa fie corect
    # pygame.time.get_ticks() -> timpul total trecut de la pornirea jocului
    # scadem timpul deja consumat inainte de salvare
    # start_ticks = pygame.time.get_ticks() - (TIME_LIMIT_SECONDS - remaining_time) * 1000
    # pornim cronometrul de la momentul continue
    # timpul ramas va fi scazut DIRECT in update_timer
    start_ticks = pygame.time.get_ticks()


    # returnam toate variabilele refacute pentru a continua jocul
    return (screen, board, board_size, score, best_score, game_over,
            timed_mode, obstacle_mode, difficulty_obstacles,
            moves_left, undo_stack, redo_stack, has_won,
            win_screen_active, start_ticks)
