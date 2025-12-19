import pygame
import sys
from graphics import TEXT_COLOR_DARK

#functia afiseaza un ecran cu intrebarea referitoare la obstacole
def choose_obstacle_mode(screen):
    #luam lungimea si latimea ferestrei pentru a centra textul
    width = screen.get_width()
    height = screen.get_height()
    font = pygame.font.SysFont("arial", 32, bold=True)

    while True:
        for event in pygame.event.get():
            #daca apasam x jocul se inchide complet
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #apasam O pentru modul cu obstacole
                if event.key == pygame.K_o:
                    return True
                #apasam N pentru modul normal,fara obstacole
                if event.key == pygame.K_n:
                    return False
        #umplem ecranul cu o culoare de fundal
        screen.fill((200, 190, 180))
        title_surface = font.render("Mod Obstacole?", True, TEXT_COLOR_DARK)
        options_surface = font.render("[O] Obstacole   |   [N] Normal", True, TEXT_COLOR_DARK)
        title_rect = title_surface.get_rect(center=(width // 2, height // 2 - 60))
        options_rect = options_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(title_surface, title_rect)
        screen.blit(options_surface, options_rect)
        pygame.display.flip()


def choose_obstacle_difficulty(screen):
    width = screen.get_width()
    height = screen.get_height()
    font = pygame.font.SysFont("arial", 32, bold=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return "easy"
                if event.key == pygame.K_h:
                    return "hard"

        screen.fill((200, 190, 180))
        title_surface = font.render("Dificultate obstacole:", True, TEXT_COLOR_DARK)
        options_surface = font.render("[E] Easy   |   [H] Hard", True, TEXT_COLOR_DARK)
        title_rect = title_surface.get_rect(center=(width // 2, height // 2 - 60))
        options_rect = options_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(title_surface, title_rect)
        screen.blit(options_surface, options_rect)
        pygame.display.flip()


def choose_moves_mode(screen):
    width = screen.get_width()
    height = screen.get_height()
    font = pygame.font.SysFont("arial", 32, bold=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    return "choose"
                if event.key == pygame.K_n:
                    return None

        screen.fill((200, 190, 180))
        title_surface = font.render("Mod cu mutari limitate?", True, TEXT_COLOR_DARK)
        options_surface = font.render("[L] Da   |   [N] Normal", True, TEXT_COLOR_DARK)
        title_rect = title_surface.get_rect(center=(width // 2, height // 2 - 60))
        options_rect = options_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(title_surface, title_rect)
        screen.blit(options_surface, options_rect)
        pygame.display.flip()


def choose_moves_difficulty(screen):
    width = screen.get_width()
    height = screen.get_height()
    font = pygame.font.SysFont("arial", 32, bold=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return 250
                if event.key == pygame.K_m:
                    return 180
                if event.key == pygame.K_h:
                    return 120

        screen.fill((200, 190, 180))
        title_surface = font.render("Alege dificultatea mutarilor:", True, TEXT_COLOR_DARK)
        options_surface = font.render("[E] Easy   |  [M] Medium   |  [H] Hard ",True, TEXT_COLOR_DARK)
        title_rect = title_surface.get_rect(center=(width // 2, height // 2 - 60))
        options_rect = options_surface.get_rect(center=(width // 2, height // 2)) 
        screen.blit(title_surface, title_rect)
        screen.blit(options_surface, options_rect)
        pygame.display.flip()

