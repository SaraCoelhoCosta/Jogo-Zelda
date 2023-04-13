from draw_map import draw_points
from algorithm import algorithm
from map import  get_dungeon1, get_dungeon2, get_dungeon3

def play(win, second_win, size_win, hyrule):
    order_way = []
    order_way = best_way(win, size_win, hyrule)
    end = hyrule.points[1][2]

    for row in hyrule.points:
            for point in row:
                point.update_neighbors(hyrule.points)

    algorithm(lambda:draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points, order_way[0].start_hyrule, hyrule.start) # Início para dungeon

    for i, dungeon in enumerate(order_way): # Percorrendo as dungers
        for row in dungeon.points:
            for point in row:
                point.update_neighbors(dungeon.points)

        algorithm(lambda:draw_points(second_win, size_win, dungeon.size, dungeon.points), dungeon.points, dungeon.end, dungeon.start) # Percorre dungeon até pingente
        algorithm(lambda:draw_points(second_win, size_win, dungeon.size, dungeon.points), dungeon.points, dungeon.start, dungeon.end) # Retorna para entrada da dungeon
                    
        if i < len(order_way) - 1:
            algorithm(lambda:draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points, order_way[i + 1].start_hyrule, dungeon.start_hyrule) # Percorre o Hyrule até a próxima dungeon
        else:
            algorithm(lambda:draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points, end, dungeon.start_hyrule) # Percorre o Hyrule para o final
        
def best_way(win, size_win, hyrule):
        for row in hyrule.points:
            for point in row:
                point.update_neighbors(hyrule.points)

        start = hyrule.start
        dungeons = [get_dungeon1(size_win), get_dungeon2(size_win), get_dungeon3(size_win)]
        best_way = []
        while dungeons:
            all_paths = []
            for dungeon in dungeons:
                path = algorithm(lambda: draw_points(win, size_win, hyrule.size, hyrule.points), hyrule.points,
                                     dungeon.start_hyrule, start, True)  # Retorna caminho entre posição inicial ou de uma dungeon comoutra dungeon
                all_paths.append((dungeon, path)) # Guarda posição da dungeon e caminho percorrido

            shortest_path = list()
            shortest_distance = float('inf')

            for dungeon, path in all_paths:  # Percorre a lista de caminhos para ver qual é o menor
                distance = len(path)
                if distance < shortest_distance:
                    shortest_distance = distance
                    shortest_path = path

            print(f'Start: {start.get_location()}, shortest path: {shortest_path[0].get_location()}, distance: {shortest_distance}')
        
            for d in dungeons:
                if d.start_hyrule == shortest_path[0]:
                    best_way.append(d)
                    dungeons.remove(d)
        
        return best_way
