import sys
import pygame
from draw_map import draw_points
from algorithm import algorithm
from map import get_hyrule, get_dungeon1, get_dungeon2, get_dungeon3

SIZE = 672 # Tamanho da janela
WINDOW = pygame.display.set_mode((SIZE, SIZE))  # Tamanho da janela
pygame.display.set_caption('Zelda com A*')  # Título

def main(win=WINDOW, size_win=SIZE):
    hyrule = get_hyrule(size_win)

    run = True
    while run:
        draw_points(win, size_win, hyrule.size, hyrule.points)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: # Sair ou encerrar programa
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_c: # Limpa o mapa
                    hyrule = get_hyrule(size_win)

                if event.key == pygame.K_SPACE:
                    for row in hyrule.points:
                        for point in row:
                            point.update_neighbors(hyrule.points)

                    algorithm(lambda:draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points, hyrule.start, hyrule.end)


if __name__ == '__main__':
    main()
