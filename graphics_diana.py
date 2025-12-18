import pygame
import sys

from graphics import *



def choose_time_mode(screen):
    """
    Functie care intreaba jucatorul daca vrea joc cu timp sau normal.
    T -> joc cu timp
    N sau ENTER -> joc normal
    Returneaza True daca modul este cu timp, False daca este normal.
    """

    # luam dimensiunile ferestrei pentru a centra textul
    width = screen.get_width()
    height = screen.get_height()

    # fonturi folosite pentru titlu si instructiuni
    title_font = pygame.font.SysFont("arial", 40, bold=True)
    text_font = pygame.font.SysFont("arial", 28)

    # variabila de control a buclei
    running = True

    # valoarea default: joc normal (fara timp)
    timed_mode = False

    # bucla se repeta pana apasam T, N sau ENTER
    while running:

        # citim toate evenimentele din coada pygame
        for event in pygame.event.get():

            # daca utilizatorul inchide fereastra -> iesim din joc complet
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # daca o tasta a fost apasata
            if event.type == pygame.KEYDOWN:

                # tasta T -> activam modul cu timp
                if event.key == pygame.K_t:
                    timed_mode = True
                    running = False  # iesim din ecranul de selectie

                # tasta N sau ENTER -> modul normal
                elif event.key == pygame.K_n or event.key == pygame.K_RETURN:
                    timed_mode = False
                    running = False  # iesim din ecranul de selectie

        # coloram fundalul cu culoarea stabilita
        screen.fill(BACKGROUND_COLOR)

        # titlu
        title_surface = title_font.render("Mod de joc", True, TEXT_COLOR_DARK)

        # get_rect() ne ajuta sa centram textul usor
        # center=(x, y) -> pozitioneaza centrul textului in mijlocul ecranului, putin mai sus
        title_rect = title_surface.get_rect(
            center=(width // 2, height // 2 - 80))

        # desenam textul in fereastra
        screen.blit(title_surface, title_rect)

        #linia 1
        line1 = text_font.render("Apasa T pentru joc CU timp", True, TEXT_COLOR_DARK)

        # centram folosind doar width si get_width
        line1_x = width // 2 - line1.get_width() // 2
        line1_y = height // 2 - 10
        screen.blit(line1, (line1_x, line1_y))

        # linia 2
        line2 = text_font.render("Apasa N sau ENTER pentru joc NORMAL", True, TEXT_COLOR_DARK)

        line2_x = width // 2 - line2.get_width() // 2
        line2_y = height // 2 + 40
        screen.blit(line2, (line2_x, line2_y))

        # actualizam fereastra cu toate schimbarile
        pygame.display.flip()

    # dupa iesirea din bucla, returnam ce mod a fost ales
    return timed_mode

def draw_undo_redo_panel(screen, font,
                         score_box_rect, best_box_rect, moves_box_rect,
                         timed_mode, remaining_time, game_over):
    """
    Deseneaza casetele UNDO, REDO si TIME sub zona HUD.
    HUD = zona de sus unde sunt SCORE / BEST / MOVES.
    """

    # Latimea si inaltimea casutelor UNDO / REDO
    help_box_width = 180
    help_box_height = 60

    # Distanta pe verticala intre HUD si casutele UNDO/REDO
    space_y = 20

    # HUD incepe in stanga exact unde incepe casuta SCORE
    hud_left = score_box_rect.left

    # Daca avem MOVES, HUD se termina in partea dreapta a casutei MOVES
    if moves_box_rect is not None:
        hud_right = moves_box_rect.right
    else:
        # Daca nu avem MOVES, HUD se termina in partea dreapta a casutei BEST
        hud_right = best_box_rect.right

    # Calculam centrul HUD-ului
    # Il folosim pentru a centra UNDO si REDO perfect la mijlocul HUD-ului
    hud_center = (hud_left + hud_right) // 2

    # Le punem sub casutele HUD, cu putin spatiu intre ele
    undo_redo_y = score_box_rect.bottom + space_y


    # Daca jocul s-a terminat, afisam culori umbrite
    if game_over:
        undo_color = undo_color_disabled
        redo_color = redo_color_disabled
        undo_text_color = undo_text_disabled
        redo_text_color = redo_text_disabled
    else:
        # Daca jocul nu s-a terminat, afisam culorile normal
        undo_color = undo_color_normal
        redo_color = redo_color_normal
        undo_text_color = undo_text_normal
        redo_text_color = redo_text_normal


    # Pozitionam UNDO la stanga centrului HUD
    undo_x = hud_center - help_box_width - 10

    # Cream un dreptunghi cu rect cu pozitia si dimensiunile lui UNDO
    # undo_x- pozitia orizontala, undo_redo_y- pozitia verticala,
    # help_box_width- latime, help_box_height- inaltime
    undo_rect = pygame.Rect(undo_x, undo_redo_y,
                            help_box_width, help_box_height)

    # Desenam casuta UNDO pe ecran
    # border_radius- pentru colturi rotunjite
    pygame.draw.rect(screen, undo_color, undo_rect, border_radius=7)

    # Scriem textul "UNDO : Z" in casuta
    undo_text = font.render("UNDO : Z", True, undo_text_color)

    # Pozitionam textul exact la centru in interiorul cutiei
    screen.blit(undo_text, undo_text.get_rect(center=undo_rect.center))

    # Pozitionam REDO la dreapta centrului HUD
    redo_x = hud_center + 10

    # Cream casuta REDO
    redo_rect = pygame.Rect(redo_x, undo_redo_y,
                            help_box_width, help_box_height)

    # Desenam casuta REDO
    pygame.draw.rect(screen, redo_color, redo_rect, border_radius=7)

    # Textul pt REDO
    redo_text = font.render("REDO : Y", True, redo_text_color)

    # Pozitionam textul in centrul casutei REDO
    screen.blit(redo_text, redo_text.get_rect(center=redo_rect.center))

    # Daca jucam intr-un mod cu timp, desenam casuta timpului
    if timed_mode:
        # Dimensiuni casuta TIME
        time_box_width = 200
        time_box_height = 45

        # Pozitionam TIME centrata sub UNDO/REDO
        time_box_x = hud_center - time_box_width // 2
        time_box_y = undo_redo_y + help_box_height + 10

        # Daca timpul este mic, coloram rosu casuta
        if remaining_time <= 10:
            time_color = (200, 50, 50) # rosu
        else:
            time_color = (150, 150, 150) # gri

        # Cream o casuta pentru TIME
        time_rect = pygame.Rect(time_box_x, time_box_y,
                                time_box_width, time_box_height)

        # O desenam
        pygame.draw.rect(screen, time_color, time_rect, border_radius=7)

        # Calculam minutele impartind la 60
        minutes = remaining_time // 60

        # Calculam secundele ramase dupa minute
        seconds = remaining_time % 60

        # Transformam minutele si secundele in text de forma mm:ss
        t_str = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)

        # Scriem textul pt TIME
        time_text = font.render("TIME: " + t_str, True, (255, 255, 255))

        # Afisam textul pt TIME centrat in casuta
        screen.blit(time_text, time_text.get_rect(center=time_rect.center))


def update_timer(start_ticks, timed_mode, game_over):
    # Daca jocul NU este in mod cu timp,
    # nu avem ce calcula -> intoarcem 0
    # si starea curenta de game_over
    if not timed_mode:
        return 0, game_over

    # pygame.time.get_ticks()
    # returneaza cate milisecunde au trecut
    # de la pornirea jocului (pygame.init)
    #
    # start_ticks = momentul cand a inceput jocul
    #
    # Diferenta dintre ele = cat timp a trecut
    mili_seconds = pygame.time.get_ticks() - start_ticks

    # Transformam milisecundele in secunde
    seconds = mili_seconds // 1000

    # Daca timpul trecut este mai mare sau egal
    # cu limita maxima (TIME_LIMIT_SECONDS)
    # inseamna ca timpul a expirat
    if seconds >= TIME_LIMIT_SECONDS:
        game_over = True
        # secundele trecute vor fi exact timpul maxim
        seconds = TIME_LIMIT_SECONDS

    # Calculam timpul ramas
    # timpul total - timpul care a trecut
    remaining_time = TIME_LIMIT_SECONDS - seconds

    # Returnam:
    # - timpul ramas
    # - daca jocul s-a terminat sau nu
    return remaining_time, game_over


def draw_all(screen, board, font, score, best_score, moves_left,
             remaining_time, timed_mode, game_over, is_new_best,
             has_won, win_screen_active):

    # draw_board:
    # deseneaza tabla
    # deseneaza scorul, best score, mutarile, timpul
    # returneaza dreptunghiurile pentru HUD:
    # score_rect- pozitia scorului
    # best_rect- pozitia best score
    # moves_rect- pozitia mutarilor (sau None)
    score_rect, best_rect, moves_rect = draw_board(
        screen, board, font, score, best_score,
        moves_left, remaining_time, timed_mode,
        game_over, is_new_best, has_won, win_screen_active
    )

    # Desenam panoul de UNDO / REDO si TIME
    # Acesta foloseste pozitiile HUD-ului
    # ca sa fie centrat corect sub ele
    draw_undo_redo_panel(
        screen, font,
        score_rect, best_rect, moves_rect,
        timed_mode, remaining_time, game_over
    )

    # pygame.display.flip()
    # face update la ecran
    # tot ce am desenat devine vizibil
    pygame.display.flip()

