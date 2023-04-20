import pygame

BLACK = (0, 0, 0)

def draw_points(win, size_win, size_map, points_map, current_map, get_object=False): # Desenha os pontos do mapa
    for row in points_map:
        for point in row:
            point.draw(win)
    draw_line(win, size_win, size_map)

    if current_map:
        if current_map.title == '# HYRULE': # Adiciona portas nas Dungeons e espada
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/portal_7.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start_hyrule_1.get_location()[1] * points_map[0][0].size, current_map.start_hyrule_1.get_location()[0] * points_map[0][0].size))
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/portal_7.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start_hyrule_2.get_location()[1] * points_map[0][0].size, current_map.start_hyrule_2.get_location()[0] * points_map[0][0].size))
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/portal_7.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start_hyrule_3.get_location()[1] * points_map[0][0].size, current_map.start_hyrule_3.get_location()[0] * points_map[0][0].size))
            if not get_object:  # Mostra a espada enquanto link não chegar nela
                win.blit(pygame.transform.scale(pygame.image.load('./sprites/sword.png'), (points_map[0][0].size, points_map[0][0].size)), (2 * points_map[0][0].size, 1 * points_map[0][0].size))
            
        else: # Adiciona portas nas Dungeons e pingentes
            win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/portal_7.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.start.get_location()[1] * points_map[0][0].size, current_map.start.get_location()[0] * points_map[0][0].size))
            if not get_object:  # Mostra a moeda enquanto link não chegar nela
                win.blit(pygame.transform.scale(pygame.image.load('./sprites/gold_coin.png'), (points_map[0][0].size, points_map[0][0].size)), (current_map.end.get_location()[1] * points_map[0][0].size, current_map.end.get_location()[0] * points_map[0][0].size))

    pygame.display.update()


def draw_line(win, size_win, size_map):  # Desenha as linhas e colunas (divisões)
    gap = size_win // size_map 

    for i in range(size_map):
        pygame.draw.line(win, BLACK, (0, i * gap), (size_win, i * gap))
        for j in range(size_map):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, size_win))

