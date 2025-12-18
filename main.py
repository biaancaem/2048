import pygame
import sys
import os

from graphics import *
from graphics_diana import *
from board_init import *
from moves_logic import *
from obstacole_options import *
from save_load import *
# ================== MAIN ==================


def main():
    pygame.init()

    #dd
    pygame.mixer.init()
    warning_sound = pygame.mixer.Sound("warning.wav")
    warning_playing = False
    # Font pentru numere
    font = pygame.font.SysFont("arial", 36, bold=True)



    # Fereastra pentru ecranul de start (mărime fixă, de exemplu 700x600)
    START_WIDTH, START_HEIGHT = 700, 600
    start_screen = pygame.display.set_mode((START_WIDTH, START_HEIGHT))
    
    show_logo_screen(start_screen)
    saved_state = load_game()

    if saved_state is not None:
        saved_time = saved_state.get("remaining_time", None)
        if saved_state.get("timed_mode", False) and saved_time == 0:
            os.remove(SAVE_FILE)
            saved_state = None

    if saved_state is not None:
        saved_choice = ask_continue_screen(start_screen)
        # ❗️ Dacă utilizatorul alege N → ștergem salvarea
        if saved_choice is None:
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
    else:
        saved_choice = None


    if saved_choice is not None:
        # → continuăm joc salvat
        (screen, board, board_size, score, best_score, game_over,
         timed_mode, obstacle_mode, difficulty,
         moves_left,
         undo_stack, redo_stack, has_won, win_screen_active,
         start_ticks) = load_saved_game_and_setup(saved_state)

    else:
        # → joc nou
        (screen, board, board_size, score, best_score, game_over,
         timed_mode, obstacle_mode, difficulty,
         moves_left,
         undo_stack, redo_stack, has_won, win_screen_active,
         start_ticks) = start_new_game(start_screen)



    # stabilim dificultatea obstacolelor (daca nu exista, punem none)
    difficulty_obstacles = difficulty if obstacle_mode else "none"

    # stabilim dificultatea mutarilor (None daca mod normal)
    difficulty_moves_str = moves_left if moves_left is not None else None


    # dd
    # generam numele fisierului de best score
    best_file = get_best_score_filename(
        board_size,
        timed_mode,
        obstacle_mode,
        difficulty_obstacles,
        difficulty_moves_str
    )

    # dd
    # incarcam best score pentru acest mod
    best_score = load_best_score(best_file)


    #cronometru
    is_new_best = False
    clock = pygame.time.Clock()
    running = True


   


    while running:
    # Evenimente
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and not game_over:
                #dd

                # dacă win-screen este activ → doar tasta C merge
                if win_screen_active:
                    if event.key == pygame.K_c:
                        win_screen_active = False   # continuăm jocul
                    # orice altă tastă este ignorată
                    continue
                
                # =========================
                #   CTRL+Z = UNDO
                # =========================
                if event.key == pygame.K_z:
                    if undo_stack:
                        # mutam starea curenta in redo_stack
                        redo_stack.append((
                            [row[:] for row in board],
                            score
                        ))
                        prev_board, prev_score = undo_stack.pop()

                        # revenim la starea anterioara
                        board = [row[:] for row in prev_board]
                        score = prev_score

                        # daca suntem in mod cu mutari limitate → consumam o mutare
                        if moves_left is not None and moves_left > 0:
                            moves_left -= 1

                    # nu mai procesam nimic la tasta asta
                    continue


                # =========================
                #         REDO (Y)
                # =========================
                if event.key == pygame.K_y:
                    if redo_stack:
                        # salvam starea curenta in undo_stack
                        undo_stack.append((
                            [row[:] for row in board],
                            score
                        ))

                        next_board, next_score = redo_stack.pop()

                        # revenim la starea refacuta
                        board = [row[:] for row in next_board]
                        score = next_score

                        # consumam o mutare (la fel ca la undo)
                        if moves_left is not None and moves_left > 0:
                            moves_left -= 1

                    continue


                if event.type == pygame.QUIT:
                    if warning_playing:
                        warning_sound.stop()
                    running = False

                if event.key == pygame.K_ESCAPE:
                    if warning_playing:
                        warning_sound.stop()
                    running = False



                direction = None

                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"


                if direction is not None:
                    # dd
                    redo_stack.clear()


                    new_board, gain, valid_move = move_board(board, direction)

                    if valid_move:
                        #dd
                        # =============================
                        # SALVAM STAREA INAINTE DE MUTARE
                        # (adica starea CURENTA, inainte de overwrite)
                        # =============================
                        undo_stack.append((
                            [row[:] for row in board],   # copie adanca a tablei
                            score,                         # scorul curent
                        ))


                        board = new_board
                        score += gain

                        # ---- salvam best score imediat ----
                        if score > best_score:
                            best_score = score
                            save_best_score(best_file, best_score)
                            is_new_best = True
                        else:
                            is_new_best = False



                        board = add_nr_random(board)
                        remaining_time, game_over = update_timer(start_ticks, timed_mode, game_over)

                        state = {
                            "board": board,
                            "score": score,
                            "best_score": best_score,
                            "moves_left": moves_left,
                            "timed_mode": timed_mode,
                            "remaining_time": remaining_time,
                            "obstacle_mode": obstacle_mode,
                            "difficulty_obstacles": difficulty_obstacles,
                            "undo_stack": undo_stack,
                            "redo_stack": redo_stack,
                        }
                        save_game(state)


                        # -----------------------
                        # DETECTARE WIN
                        # -----------------------
                        if not has_won:
                            for r in range(board_size):
                                for c in range(board_size):
                                    if board[r][c] == 2048:
                                        has_won = True
                                        win_screen_active = True

                        if moves_left is not None:
                            moves_left -= 1
                            if moves_left <= 0:
                                game_over = True

                        if not any_moves_possible(board):
                            game_over = True

                        if score > best_score:
                            best_score = score
                            is_new_best = True
                        else:
                            is_new_best = False


            if event.type == pygame.QUIT:
                running = False

        remaining_time, game_over = update_timer(
            start_ticks, timed_mode, game_over
        )

        # Play beep at each second in the last 10 seconds
        if timed_mode:
            if remaining_time <= 10 and not warning_playing:
                warning_sound.play(loops=-1)
                warning_playing = True

            if remaining_time == 0 and warning_playing:
                warning_sound.stop()
                warning_playing = False

        


        # -----------------------
        # DESENARE COMPLETĂ
        # -----------------------
        draw_all(
            screen, board, font,
            score, best_score, moves_left,
            remaining_time, timed_mode,
            game_over, is_new_best,
            has_won, win_screen_active
        )
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

