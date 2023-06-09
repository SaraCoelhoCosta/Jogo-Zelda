import sys
import pygame
from queue import PriorityQueue

def h(start, end):  # Heurística - quanto falta para chegar no objetivo
    x1, y1 = start
    x2, y2 = end
    return abs(x1 + x2) + abs(y1 - y2) # É calculada a distância de Manhattan

def reconstruct_path(win, came_from, current, draw):  # Função que reconstrói o caminho
    list_path = [current]
    win.blit(pygame.transform.scale(pygame.image.load('./sprites/link/link_f1.png'), (current.size, current.size)), (current.y, current.x))
    pygame.time.delay(100)
    while current in came_from:
        current = came_from[current]
        list_path.append(current)
        pygame.time.delay(60)
        draw()
        win.blit(pygame.transform.scale(pygame.image.load('./sprites/link/link_f1.png'), (current.size, current.size)), (current.y, current.x))
        pygame.display.update()
    win.blit(pygame.transform.scale(pygame.image.load('./sprites/link/link_f1.png'), (current.size, current.size)), (current.y, current.x))
    return list_path

# Algoritmo A*
def algorithm(win, draw, map_points, start_point, end_point, best_way=False):
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
                return list(reversed(reconstruct_path(win, came_from, current, draw))) # Inverte a lista para voltar do ponto final para o inicial
            else:
                list_path = [current]
                while current in came_from:
                    current = came_from[current]
                    list_path.append(current)
                return list(reversed(list_path))

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + neighbor.cost # G(nó) temporrária para calcular o custo do caminho de ir para os vizinhos

            if temp_g_score < g_score[neighbor]: # Compara os custos de deslocamento
                came_from[neighbor] = current # O caminho na posição do vizinho recebe a posição atual

                g_score[neighbor] = temp_g_score # Custo do nó vizinho recebe o custo temporário
                f_score[neighbor] = temp_g_score + h(neighbor.get_location(), end_point.get_location()) # Custo total do nó vizinho recebe o custo temporário + a heurística desse nó até o objetivo

                if neighbor not in open_set: # Se o nó vizinho ainda não está na lista aberta, ou seja, já foi visitado
                    count += temp_g_score # Adiciona-se o custo do vizinho visitado
                    closed_set.put((f_score[neighbor], count, neighbor)) # Atualiza-se a lista de 
                    open_set.add(neighbor) 
