import pygame

BLACK = (0, 0, 0) # Tupla RGB que indica a cor das bordas de cada quadradinho

def draw_points(win, size_win, size_map, points_map, current_map, get_object=False): # Desenha os pontos do mapa, que rodarão sempre
    for row in points_map: # For que percorre cada linha nos pontos do mapa
        for point in row: # For que percorre cada ponto da linha
            point.draw(win) # Desenha pontos na janela
    draw_line(win, size_win, size_map) # Função que desenha as bordas de cada ponto (quadrado do mapa)

    if current_map:
        if current_map.title == '# HYRULE': # Adiciona portas nas Dungeons e espada no mapa principal
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/dungeon.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start_hyrule_1.get_location()[1] * points_map[0][0].size, current_map.start_hyrule_1.get_location()[0] * points_map[0][0].size))
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/dungeon.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start_hyrule_2.get_location()[1] * points_map[0][0].size, current_map.start_hyrule_2.get_location()[0] * points_map[0][0].size))
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/dungeon.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start_hyrule_3.get_location()[1] * points_map[0][0].size, current_map.start_hyrule_3.get_location()[0] * points_map[0][0].size))
            if not get_object:  # Mostra a espada enquanto link não chegar nela
                win.blit(pygame.transform.scale(pygame.image.load('./sprites/sword.png'), (points_map[0][0].size, points_map[0][0].size)), (2 * points_map[0][0].size, 1 * points_map[0][0].size))
            
        else: # Adiciona portas nas Dungeons e os pingentes
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/dungeon.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start.get_location()[1] * points_map[0][0].size, current_map.start.get_location()[0] * points_map[0][0].size))
            if not get_object:  # Mostra o pingente enquanto Link (agente) não chegar nela
                win.blit(pygame.transform.scale(pygame.image.load('./sprites/pingente1.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.end.get_location()[1] * points_map[0][0].size, current_map.end.get_location()[0] * points_map[0][0].size))

    pygame.display.update() # Atualização constante do mapa


def draw_line(win, size_win, size_map):  # Desenha as linhas e colunas (divisões), ou seja, desenha as bordas de cada ponto do mapa
    gap = size_win // size_map # gap recebe o tamanho ideal para cada ponto ter o mesmo tamanho

    for i in range(size_map):
        pygame.draw.line(win, BLACK, (0, i * gap), (size_win, i * gap)) # Insere bordas nas linhas
        for j in range(size_map):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, size_win)) # Insere bordas nas colunas

