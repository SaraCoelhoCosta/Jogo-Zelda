import itertools
from draw_map import draw_points
from algorithm import algorithm
from map import  get_dungeon1, get_dungeon2, get_dungeon3

def play(win, second_win, size_win, hyrule):
    order_way = best_way(win, size_win, hyrule) # Recebe a ordem em que as dungers serão percorridas
    end = hyrule.points[1][2]
    # end = hyrule.end
    distance_total = 0
    
    path = algorithm(win, lambda:draw_points(win, size_win, hyrule.size, hyrule.points, hyrule), hyrule.points, order_way[0].start_hyrule_1, hyrule.start) # Início para dungeon
    distance = calculate_path(path)
    distance_total = distance_total + distance
    print(f'Início para dungeon 1: {distance}')

    for i, dungeon in enumerate(order_way): # Percorrendo as dungers
        for row in dungeon.points:
            for point in row:
                point.update_neighbors(dungeon.points)

        path = algorithm(win, lambda:draw_points(second_win, size_win, dungeon.size, dungeon.points, dungeon), dungeon.points, dungeon.end, dungeon.start) # Percorre dungeon até pingente
        distance = calculate_path(path)
        distance_total = distance_total + distance
        print(f'Percorrendo dungeon {i+1}: {distance}')
        
        path = algorithm(win, lambda:draw_points(second_win, size_win, dungeon.size, dungeon.points, dungeon, True), dungeon.points, dungeon.start, dungeon.end) # Retorna para entrada da dungeon
        distance = calculate_path(path)
        distance_total = distance_total + distance
        print(f'Retornando para início da dungeon {i+1}: {distance}')
                    
        if i < len(order_way) - 1:
            path = algorithm(win, lambda:draw_points(win, size_win, hyrule.size, hyrule.points, hyrule), hyrule.points, order_way[i + 1].start_hyrule_1, dungeon.start_hyrule_1) # Percorre o Hyrule até a próxima dungeon
            distance = calculate_path(path)
            distance_total = distance_total + distance
            print(f'Percorrendo hyrule para dungeon {i+2}: {distance}')
        else:
            path = algorithm(win, lambda:draw_points(win, size_win, hyrule.size, hyrule.points, hyrule), hyrule.points, end, dungeon.start_hyrule_1) # Percorre o Hyrule para o final
            distance = calculate_path(path)
            distance_total = distance_total + distance
            print(f'Percorrendo da dungeon {i+1} para o fim: {distance}')
    print(f'Distância total percorrida: {distance_total}')

    return True
        
def best_way(win, size_win, hyrule):
        
        for row in hyrule.points:
            for point in row:
                point.update_neighbors(hyrule.points)

        dungeons = [get_dungeon1(size_win), get_dungeon2(size_win), get_dungeon3(size_win)]

        perm_list = []
        perms = list(itertools.permutations(dungeons)) # Criando permutação com todas as possibilidades
        for perm in perms:  # Convertendo elementos da permutação em lista
            perm_list.append(list(perm))

        all_paths = []
        for ways_list in perm_list:
            start = hyrule.start
            # end = hyrule.end
            end = hyrule.points[1][2]
            distance_total = 0
            points_dungeon = []
            for i, dungeon in enumerate(ways_list):
                path = algorithm(win, lambda: draw_points(win, size_win, hyrule.size, hyrule.points, hyrule), hyrule.points,
                                     dungeon.start_hyrule_1, start, True)  # Retorna caminho entre posição inicial ou de uma dungeon com outra dungeon
                start = dungeon.start_hyrule_1
                distance = calculate_path(path)
                distance_total = distance_total + distance
                
                if i == len(ways_list) - 1:
                    path = algorithm(win, lambda: draw_points(win, size_win, hyrule.size, hyrule.points, hyrule), hyrule.points,
                                     end, dungeon.start_hyrule_1, True)  # Retorna caminho entre posição inicial ou de uma dungeon com outra dungeon
                    distance = calculate_path(path)
                    distance_total = distance_total + distance
                    
                # points_dungeon.append(dungeon.start_hyrule_1.get_location())     
                points_dungeon.append(dungeon)     
            all_paths.append((points_dungeon, distance_total)) # Guarda posição da dungeon e caminho percorrido
            # print(f'Interação: {points_dungeon, distance_total}')
        
        shortest_path = list()
        shortest_distance = float('inf')
        for dungeon, distance in all_paths:  # Percorre a lista de caminhos para ver qual é o menor
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = dungeon
        
        # print(f'\nShortest path: {shortest_path}, distance: {shortest_distance}')
        return shortest_path

def calculate_path(path):
    distance = 0
    for point in path:
        distance = distance + point.cost
    return distance