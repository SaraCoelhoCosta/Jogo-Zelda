import sys
import pygame
from queue import PriorityQueue

def h(start, end):  # Heurística - quanto falta para chegar no objetivo
    x1, y1 = start
    x2, y2 = end
    return abs(x1 + x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):  # TODO: refazer
    list_path = [current]
    while current in came_from:
        current = came_from[current]
        list_path.append(current)
        if current.color == (128, 0, 128):
            current.make_path2()
        else:    
            current.make_path()
        pygame.time.delay(80)
        draw()
    return list_path

# Algoritmo A*
def algorithm(draw, map_points, start_point, end_point, best_way=False):
    came_from = {}
    count = 0

    # Lista aberta - nós a serem visitados
    open_set = {start_point}

    # Lista fechada - nós visitados
    closed_set = PriorityQueue()
    closed_set.put((0, count, start_point))

    # Quanto foi deslocado do nó inicial até o nó atual
    g_score = {point: float("inf") for row in map_points for point in row}
    g_score[start_point] = 0

    # Quanto falta deslocar do nó atual até o nó objetivo
    f_score = {point: float("inf") for row in map_points for point in row}
    f_score[start_point] = h(start_point.get_location(), end_point.get_location())

    # Executa o algoritmo enquanto a fila com vizinhos não visitados não for vazia
    while not closed_set.empty():

        # Sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        current = closed_set.get()[2]
        open_set.remove(current)

        list_path = []
        # Verifica se o nó atual é o objetivo, caso seja, ele constrói o caminho e retorna o caminho feito
        if current == end_point:
            if best_way == False:
                return list(reversed(reconstruct_path(came_from, current, draw)))
            else:
                list_path = [current]
                while current in came_from:
                    current = came_from[current]
                    list_path.append(current)
                return list(reversed(list_path))

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + neighbor.cost

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current

                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_location(), end_point.get_location())

                if neighbor not in open_set:
                    count += temp_g_score
                    closed_set.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)
