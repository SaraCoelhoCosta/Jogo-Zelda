import sys
import pygame
from draw_map import draw_points
from algorithm import algorithm
from map import get_hyrule, get_dungeon1, get_dungeon2, get_dungeon3

SIZE = 672 # Tamanho da janela
WINDOW = pygame.display.set_mode((SIZE, SIZE))  # Tamanho da janela
SECOND_WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Zelda com A*')  # Título

def main(win=WINDOW, size_win=SIZE):
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
                    for row in hyrule.points:
                        for point in row:
                            point.update_neighbors(hyrule.points)

                    algorithm(lambda:draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points, hyrule.start, hyrule.points[1][24]) # inicio p/ dungeon1
                    dungeon1 = get_dungeon1(size_win) # abre dungeon1
                    for row in dungeon1.points:
                        for point1 in row:
                            point1.update_neighbors(dungeon1.points)

                    algorithm(lambda:draw_points(SECOND_WINDOW, size_win, dungeon1.size, dungeon1.points), dungeon1.points, dungeon1.start, dungeon1.end) # percorre dungeon1
                    

                    algorithm(lambda:draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points, hyrule.points[1][24], hyrule.points[17][39]) # dungeon1 p/ dungeon2
                    dungeon2 = get_dungeon2(size_win) # abre dungeon2
                    for row in dungeon2.points:
                        for point2 in row:
                            point2.update_neighbors(dungeon2.points)
                    algorithm(lambda:draw_points(SECOND_WINDOW, size_win, dungeon2.size, dungeon2.points), dungeon2.points, dungeon2.start, dungeon2.end) # percorre dungeon2
                    


                    algorithm(lambda:draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points, hyrule.points[17][39], hyrule.points[32][5]) # dungeon2 p/ dungeon3
                    dungeon3 = get_dungeon3(size_win) # abre dungeon3
                    for row in dungeon3.points:
                        for point3 in row:
                            point3.update_neighbors(dungeon3.points)
                    algorithm(lambda:draw_points(SECOND_WINDOW, size_win, dungeon3.size, dungeon3.points), dungeon3.points, dungeon3.start, dungeon3.end) # percorre dungeon3
                    
        
            


if __name__ == '__main__':
    main()
