import pygame
import sys
import os

from graphics import *
from graphics_diana import *
from board_init import *
from moves_logic import *
from obstacole_options import *
from save_load import *

def main():
    # initializam pygame
    pygame.init()

    # initializare sunet
    # incercam sa pornim sunetul, daca sistemul nu suporta audio jocul va rula fara sunet
    sound_enabled = True
    try:
        pygame.mixer.init()
        warning_sound = pygame.mixer.Sound("warning.wav")
    except pygame.error:
        print("audio indisponibil - rulez fara sunet")
        sound_enabled = False
        warning_sound = None

    warning_playing = False

    # initializare font
    # acest font este folosit pentru numerele de pe tabla
    font = pygame.font.SysFont("arial", 36, bold=True)
    # ecran start
    # cream o fereastra temporara pentru ecranul de start
    start_width = 700
    start_height = 600
    start_screen = pygame.display.set_mode((start_width, start_height))

    # afisam logo-ul jocului
    show_logo_screen(start_screen)

    # incercam sa incarcam un joc salvat
    saved_state = load_game()

    if saved_state is not None:
        saved_time = saved_state.get("remaining_time", None)
        if saved_state.get("timed_mode", False) and saved_time == 0:
            os.remove(SAVE_FILE)
            saved_state = None

    if saved_state is not None:
        # intrebam utilizatorul daca vrea sa continue
        saved_choice = ask_continue_screen(start_screen)

        # daca utilizatorul alege nu
        # stergem salvarea existenta
        if saved_choice is None:
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
    else:
        saved_choice = None

    # initializare joc
    if saved_choice is not None:
        # continuam jocul salvat
        (screen, board, board_size, score, best_score, game_over,
         timed_mode, obstacle_mode, difficulty,
         moves_left,
         undo_stack, redo_stack, has_won, win_screen_active,
         start_ticks) = load_saved_game_and_setup(saved_state)
    else:
        # pornim un joc nou
        (screen, board, board_size, score, best_score, game_over,
         timed_mode, obstacle_mode, difficulty,
         moves_left,
         undo_stack, redo_stack, has_won, win_screen_active,
         start_ticks) = start_new_game(start_screen)

    # setari pentru best score
    # stabilim dificultatea obstacolelor
    if obstacle_mode:
        difficulty_obstacles = difficulty
    else:
        difficulty_obstacles = "none"

    # stabilim dificultatea mutarilor
    if moves_left is not None:
        difficulty_moves_str = moves_left
    else:
        difficulty_moves_str = None

    # generam numele fisierului pentru best score
    best_file = get_best_score_filename(
        board_size,
        timed_mode,
        obstacle_mode,
        difficulty_obstacles,
        difficulty_moves_str
    )

    # incarcam best score pentru acest mod
    best_score = load_best_score(best_file)

    # variabile pentru bucla principala
    clock = pygame.time.Clock()
    running = True
    is_new_best = False

    # bucla principala a jocului

    while running:
        # procesare evenimente
        for event in pygame.event.get():

            # inchidere fereastra
            if event.type == pygame.QUIT:
                running = False

            # procesare taste
            if event.type == pygame.KEYDOWN and not game_over:

                # daca ecranul de win este activ
                # permitem doar tasta c
                if win_screen_active:
                    if event.key == pygame.K_c:
                        win_screen_active = False
                    continue

                # undo (z)
                if event.key == pygame.K_z:
                    if undo_stack:
                        redo_stack.append((copy_board(board), score))
                        prev_board, prev_score = undo_stack.pop()
                        board = copy_board(prev_board)
                        score = prev_score

                        if moves_left is not None and moves_left > 0:
                            moves_left = moves_left - 1
                    continue

                # redo (y)
                if event.key == pygame.K_y:
                    if redo_stack:
                        undo_stack.append((copy_board(board), score))
                        next_board, next_score = redo_stack.pop()
                        board = copy_board(next_board)
                        score = next_score

                        if moves_left is not None and moves_left > 0:
                            moves_left = moves_left - 1
                    continue

                # iesire cu escape
                if event.key == pygame.K_ESCAPE:
                    if warning_playing and sound_enabled:
                        warning_sound.stop()
                    running = False
                    continue

                # determinare directie (sageti + wasd)
                direction = None

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = "RIGHT"
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = "UP"
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = "DOWN"

                # aplicare mutare
                if direction is not None:
                    redo_stack.clear()

                    new_board, gain, valid_move = move_board(board, direction)

                    if valid_move:
                        undo_stack.append((copy_board(board), score))

                        board = new_board
                        score = score + gain

                        if score > best_score:
                            best_score = score
                            save_best_score(best_file, best_score)
                            is_new_best = True
                        else:
                            is_new_best = False

                        board = add_nr_random(board)

                        remaining_time, game_over = update_timer(
                            start_ticks, timed_mode, game_over
                        )

                        save_game({
                            "board": board,
                            "score": score,
                            "best_score": best_score,
                            "moves_left": moves_left,
                            "timed_mode": timed_mode,
                            "remaining_time": remaining_time,
                            "obstacle_mode": obstacle_mode,
                            "difficulty_obstacles": difficulty_obstacles,
                            "undo_stack": undo_stack,
                            "redo_stack": redo_stack
                        })

                        # verificare win
                        if not has_won:
                            r = 0
                            while r < board_size:
                                c = 0
                                while c < board_size:
                                    if board[r][c] == 2048:
                                        has_won = True
                                        win_screen_active = True
                                    c = c + 1
                                r = r + 1

                        if moves_left is not None:
                            moves_left = moves_left - 1
                            if moves_left <= 0:
                                game_over = True

                        if not any_moves_possible(board):
                            game_over = True

                        if score > best_score:
                            best_score = score
                            is_new_best = True
                        else:
                            is_new_best = False

        # update timer
        remaining_time, game_over = update_timer(
            start_ticks, timed_mode, game_over
        )

        # sunet avertizare timp
        if timed_mode and sound_enabled:
            if remaining_time <= 10 and not warning_playing:
                warning_sound.play(loops=-1)
                warning_playing = True

            if remaining_time == 0 and warning_playing:
                warning_sound.stop()
                warning_playing = False

        # desenare ecran
        draw_all(
            screen, board, font,
            score, best_score, moves_left,
            remaining_time, timed_mode,
            game_over, is_new_best,
            has_won, win_screen_active
        )

        clock.tick(60)

    # inchidere joc
    pygame.quit()
    sys.exit()


# punctul de intrare in program
if __name__ == "__main__":
    main()
