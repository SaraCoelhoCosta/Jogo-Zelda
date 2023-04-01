import pygame
# from queue import PriorityQueue
from map import make_grid, draw

SIZE = 672 # Tamanho da janela
WINDOW = pygame.display.set_mode((SIZE, SIZE))  # Tamanho da janela
pygame.display.set_caption('Zelda com A*')  # Título


def main(win=WINDOW, size=SIZE):
    #Rows = 50
    #grid = make_grid(Rows, size)

    run = True
    while run:
        draw(win, grid, Rows, size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_q: # Sair ou encerrar programa
                run = False

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    for row in grid:
                        for point in row:
                            point.update_neighbors(grid)

                    algorithm(lambda:draw(win, grid, Rows, size), grid, start, end)

                if event.key == pygame.K_c: # Limpa o mapa
                    grid = make_grid(Rows, size)

    pygame.quit()


main()
