import sys
import pygame
from draw_map import draw_points
from game import play
from map import get_hyrule

SIZE = 672 # Tamanho da janela
WINDOW = pygame.display.set_mode((SIZE, SIZE))  # Tamanho da janela
SECOND_WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Zelda com A*')  # Título

def main(win=WINDOW, second_win=SECOND_WINDOW, size_win=SIZE):
    hyrule = get_hyrule(size_win)

    run = True
    while run:
        draw_points(win, size_win, hyrule.size, hyrule.points)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: # Fecha a janela e encerra programa com o botão X
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: # Fecha a janela e encerrar programa com o Q
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_c: # Limpa o mapa
                    hyrule = get_hyrule(size_win)

                if event.key == pygame.K_SPACE:
                    play(win, second_win, size_win, hyrule)

if __name__ == '__main__':
    main()
