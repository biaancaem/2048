import pygame
import sys

TILE_SIZE = 100 #dimensiune casete
TILE_MARGIN = 20 #marginea exterioara a tablei
TILE_MARGIN_BETWEEN = 10 #spatiu intre casete
INFO_PANEL_HEIGHT = 250 #inaltimea zonei de sus care contine(score, best, moves)

#pentru mod cu timp
TIME_BOX_COLOR = (150, 150, 150)    # caseta pentru TIME (gri)
TIME_LIMIT_SECONDS = 180

#culori generale
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_COLOR = (205, 193, 180)
TEXT_COLOR_DARK = (119, 110, 101)
TEXT_COLOR_LIGHT = (249, 246, 242)

#culori casete score
SCORE_BOX_COLOR = (245, 142, 160)   # caseta pentru SCORE
BEST_BOX_COLOR  = (105, 190, 170)   # caseta pentru BEST (altă nuanță)
SCORE_TEXT_COLOR = (255, 255, 255)  # culoarea textului din casete

undo_color_normal = (180, 150, 160)
redo_color_normal = (120, 180, 160)
undo_text_normal = (255, 255, 255)
redo_text_normal = (255, 255, 255)

#culori game over
undo_color_disabled = (80, 70, 70)
redo_color_disabled = (60, 80, 80)
undo_text_disabled = (120, 120, 120)
redo_text_disabled = (120, 120, 120)



# culori pentru câteva valori
TILE_COLORS = {
    2:  (238, 228, 218),
    4:  (237, 224, 200),
    8:  (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
# FUNCTII GRAFICE

def dimensiune_fereastra(board_size):
    """Calculează lățimea/înălțimea ferestrei în funcție de mărimea tablei."""
    width = 2 * TILE_MARGIN + board_size * TILE_SIZE + (board_size - 1) * TILE_MARGIN_BETWEEN
    height = width + INFO_PANEL_HEIGHT
    # asigurăm spațiu minim pentru 3 casete sus
    min_width = 3 * 180 + 2 * 40 + 80  # casete + spațiu + margini
    width = max(width, min_width)
    return width, height

"""desenare tabla"""
def draw_board(screen, board, font, score, best_score,
               moves_left, remaining_time, timed_mode,
               game_over, is_new_best, has_won, win_screen_active):

    # Umplem toata fereastra cu culoarea de fundal
    screen.fill(BACKGROUND_COLOR)
    board_size = len(board)

    # Dimensiunea ferestrei, ca sa putem centra casetele sus
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # dimensiuni casete
    box_width = 180
    box_height = 95
    box_spacing = 40
    top_margin = 20  # marginea de sus fata de fereastra

    # Dacă avem moves - 3 casete
    # Dacă nu avem moves - 2 casete
    if moves_left is None:
        num_boxes = 2
    else:
        num_boxes = 3

    total_boxes_width = num_boxes * box_width + (num_boxes - 1) * box_spacing
    start_x = (screen_width - total_boxes_width) // 2 # = punct de inceput al casetelor
    #impartim spatiul liber in 2 pentru a centra pe orizontala casetele

    # SCORE
    score_box_x = start_x
    score_box_y = top_margin
    score_box_rect = pygame.Rect(score_box_x, score_box_y,box_width, box_height)

    # BEST
    best_box_x = score_box_x + box_width + box_spacing
    best_box_y = top_margin
    #functie pentru desenarea unui dreptunghi la coordonatele x,y
    best_box_rect = pygame.Rect(best_box_x, best_box_y, box_width, box_height)

    # MOVES (doar daca exista)
    if moves_left is not None:
        moves_box_x = best_box_x + box_width + box_spacing
        moves_box_y = top_margin
        moves_box_rect = pygame.Rect(moves_box_x, moves_box_y, box_width, box_height)

    # desenam caseta SCORE cu prima culoare
    pygame.draw.rect(screen, SCORE_BOX_COLOR, score_box_rect, border_radius=7)

    # desenam caseta BEST cu alta culoare
    pygame.draw.rect(screen, BEST_BOX_COLOR, best_box_rect, border_radius=7)

    # text in caseta SCORE

    score_label_surface = font.render("SCORE", True, SCORE_TEXT_COLOR)
    score_label_rect = score_label_surface.get_rect(
        center=(score_box_rect.centerx, score_box_rect.top + 20)
    )
    screen.blit(score_label_surface, score_label_rect)

    score_value_surface = font.render(str(score), True, SCORE_TEXT_COLOR)
    score_value_rect = score_value_surface.get_rect(
        center=(score_box_rect.centerx, score_box_rect.top + 60)
    )
    screen.blit(score_value_surface, score_value_rect)

    #text in caseta BEST
    best_label_surface = font.render("BEST", True, SCORE_TEXT_COLOR)
    best_label_rect = best_label_surface.get_rect(center=(best_box_rect.centerx, best_box_rect.top + 20))
    screen.blit(best_label_surface, best_label_rect)

    best_value_surface = font.render(str(best_score), True, SCORE_TEXT_COLOR)
    best_value_rect = best_value_surface.get_rect(center=(best_box_rect.centerx, best_box_rect.top + 60))
    screen.blit(best_value_surface, best_value_rect)

    # caseta MOVES
    if moves_left is not None:
        moves_box_x = best_box_x + box_width + box_spacing
        moves_box_y = top_margin
        moves_box_rect = pygame.Rect(moves_box_x, moves_box_y, box_width, box_height)

        pygame.draw.rect(screen, (180, 150, 90), moves_box_rect, border_radius=7)

        moves_label_surface = font.render("MOVES", True, SCORE_TEXT_COLOR)
        moves_label_rect = moves_label_surface.get_rect(center=(moves_box_rect.centerx, moves_box_rect.top + 20))
        screen.blit(moves_label_surface, moves_label_rect)

        moves_value_surface = font.render(str(moves_left), True, SCORE_TEXT_COLOR)
        moves_value_rect = moves_value_surface.get_rect(center=(moves_box_rect.centerx, moves_box_rect.top + 60))
        screen.blit(moves_value_surface, moves_value_rect)

    board_pixel_width = board_size * TILE_SIZE + (board_size - 1) * TILE_MARGIN_BETWEEN
    board_pixel_height = board_size * TILE_SIZE + (board_size - 1) * TILE_MARGIN_BETWEEN

    # centrare orizontala
    offset_x = (screen_width - board_pixel_width) // 2

    # tabla incepe sub panelul de informatii
    offset_y = INFO_PANEL_HEIGHT + TILE_MARGIN

    for row_index in range(board_size):
        for col_index in range(board_size):
            tile_value = board[row_index][col_index]

            tile_x = offset_x + col_index * (TILE_SIZE + TILE_MARGIN_BETWEEN)
            tile_y = offset_y + row_index * (TILE_SIZE + TILE_MARGIN_BETWEEN)

            if tile_value == -1: #obstacol
                tile_color = (50, 50, 50)  # gri-închis
            elif tile_value == 0: #gol
                tile_color = EMPTY_COLOR
            else: #este un tile cu numar, daca exista numarul in dictionar,foloseste culoarea
                tile_color = (60, 58, 50)
                if tile_value in TILE_COLORS:
                    tile_color = TILE_COLORS[tile_value]

            tile_rect = pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)
            #desenam tile-ul pe ecran
            pygame.draw.rect(screen, tile_color, tile_rect, border_radius=8)
            #verificam daca desenam text
            #daca desenam text, alegem o culoare cu care sa afisam textul in functie de ce nr are caseta pentru un contrast mai bun
            if tile_value != 0: #daca nu e gol,putem pune un nr acolo
                if tile_value == -1:
                    continue  # obstacol -> nu desenăm nimic
                elif tile_value <= 4:
                    text_color = TEXT_COLOR_DARK
                else:
                    text_color = TEXT_COLOR_LIGHT
                #cream o imagine cu numarul
                text_surface = font.render(str(tile_value), True, text_color)
                #cream dreptunghi invizibil si centram in tile
                text_rect = text_surface.get_rect(center=tile_rect.center)
                #desenam textul pe ecran
                screen.blit(text_surface, text_rect)


    #GAME OVER OVERLAY

    if game_over:
        # overlay
        #creez suprafata cat tot ecranul
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.set_alpha(160)  # o fac semi-transparenta
        overlay.fill((0, 0, 0)) # o coloram negru
        screen.blit(overlay, (0, 0)) # o pun peste joc

        # cream textul pt Game Over,il centram si desenam
        game_over_text = font.render("GAME OVER", True, TEXT_COLOR_LIGHT)
        go_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 40))
        screen.blit(game_over_text, go_rect)

        # afisam scorul pe care il avem in jocul curent
        score_text = font.render(f"Scor: {score}", True, TEXT_COLOR_LIGHT)
        score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2 + 10))
        screen.blit(score_text, score_rect)

        #afisam best-ul pe care l-am facut
        best_text = font.render(f"Best: {best_score}", True, TEXT_COLOR_LIGHT)
        best_rect = best_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(best_text, best_rect)

        #daca cumva bestul este mai mare decat ce era inainte, afisam un nou mesaj
        if is_new_best:
            new_best_text = font.render("NEW BEST SCORE!", True, TEXT_COLOR_LIGHT)
            newb_rect = new_best_text.get_rect(center=(screen_width // 2, screen_height // 2 + 90))
            screen.blit(new_best_text, newb_rect)


    # WIN OVERLAY
    if not game_over and has_won and win_screen_active:
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        win_text = font.render("YOU WIN!", True, (255, 255, 255))
        win_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2 - 40))
        screen.blit(win_text, win_rect)

        cont_text = font.render("Apasa C pentru a continua...", True, (255, 255, 255))
        cont_rect = cont_text.get_rect(center=(screen_width // 2, screen_height // 2 + 20))
        screen.blit(cont_text, cont_rect)

    #returneaza pozitiile casetelor
    if moves_left is not None:
        return score_box_rect, best_box_rect, moves_box_rect
    else:
        return score_box_rect, best_box_rect, None


def show_start_screen(screen):
    """
    Afiseaza ecranul de start cu:
    - titlu
    - regulile jocului
    - optiuni pentru marimea tablei (4x4, 5x5, 6x6)
    Returneaza board_size ales.
    """
    pygame.display.set_caption("2048 - Reguli și alegere dimensiune")

    title_font = pygame.font.SysFont("arial", 48, bold=True)
    text_font = pygame.font.SysFont("arial", 24)
    small_font = pygame.font.SysFont("arial", 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Alege mărimea tablei
                if event.key == pygame.K_1:
                    return 4  # 4x4 clasic
                elif event.key == pygame.K_2:
                    return 5  # 5x5
                elif event.key == pygame.K_3:
                    return 6  # 6x6

        screen.fill(BACKGROUND_COLOR)

        # Titlu
        title_surface = title_font.render("2048", True, TEXT_COLOR_DARK)
        title_rect = title_surface.get_rect(
            center=(screen.get_width() // 2, 60)
        )
        screen.blit(title_surface, title_rect)

        # Regulile jocului
        rules_lines = [
            "Reguli joc 2048:",
            "- Foloseste sagetile pentru a muta toate casetele.",
            "- Cand 2 casete cu aceeasi numar se ating,acestea se combina.",
            "- Scopul este să ajungi la caseta cu numarul 2048.",
            "  (sau să faci un scor cât mai mare :D)",
            "",
            "Alege dimensiunea tablei:",
            "[1] 4 x 4  (hard)",
            "[2] 5 x 5  (medium)",
            "[3] 6 x 6  (easy)",
        ]

        y = 140 #verticala unde incepe primul rand
        for line in rules_lines:
            line_surface = text_font.render(line, True, TEXT_COLOR_DARK)
            line_rect = line_surface.get_rect(
                center=(screen.get_width() // 2, y)
            )
            screen.blit(line_surface, line_rect)
            y += 35

        # Indicație jos
        info_surface = small_font.render("Apasă 1, 2 sau 3 pentru a începe.", True, TEXT_COLOR_DARK)
        info_rect = info_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() - 40))
        screen.blit(info_surface, info_rect)

        pygame.display.flip()

def show_logo_screen(screen):
    """
    Afiseaza imaginea 2048 pe TOT ecranul
    si textul 'Press anywhere to start'.
    Iese din functie cand apesi orice tasta sau click.
    """

    # dimensiunea ferestrei
    width = screen.get_width()
    height = screen.get_height()

    # font pentru mesaj
    menu_font = pygame.font.SysFont("arial", 30, bold=True,italic=True)

    # incarcam imaginea
    start_image = pygame.image.load("start_2048.png").convert_alpha()

    # o scalam sa fie cat tot ecranul 
    start_image = pygame.transform.smoothscale(start_image, (width, height))
    #cream un cronometru care limiteaza viteza jocului - FPS
    clock = pygame.time.Clock()
    running = True
    #bucla pincipala de rulare a ecranului de start
    while running:
        #daca exista un eveniment care s a intamplat(daca s-a apasat o tasta sau s-a facut click pe mouse) running devine false, adica iesim din ecranul de start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # orice tasta sau click -iesim din ecranul de start
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # desenam imaginea pe tot ecranul coltul stanga-sus
        screen.blit(start_image, (0, 0))

        # mesajul de jos
        #rander transforma textul intr o imagine parametrii -> mesaj,true - netezeste marginile literelor ,culoare- gri
        text_surface = menu_font.render("Press anywhere to start...", True, (200, 200, 200))
        text_rect = text_surface.get_rect(center=(width // 2, height - 34)) #se creaza un dreptunghi invizibil pentru text centat
        screen.blit(text_surface, text_rect) #deseneaza imaginea textului pe ecran(text_surface la coordonatele text_react)
        pygame.display.flip() # afisam tot ce am desenat
        #jocul e limitat la 60 de cadre pe sec
        clock.tick(60)

