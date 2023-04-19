from draw_map import make_points

maps = {}  # Variável global 
points_map_hyrule = []
class Map: # Mapa
    def __init__(self, title, size, start, end, points_map, start_hyrule):
        self.title = title
        self.size = size
        self.start = start
        self.end = end
        self.points = points_map
        self.start_hyrule = start_hyrule


def read_maps(title):
    current_map = ''

    if len(maps) != 0:
        return maps[title]
    
    elif len(maps) == 0:
        with open("maps.txt", "r") as file:  # Lê o arquivo de texto com os mapas
            lines = file.readlines()

        for line in lines:
            line = line.split('\n')[0]

            if not (line.strip()):  # Ignora linha vazia
                continue

            elif line[0] == '#':  # Verifica se a linha é igual ao título do mapa
                '''
                    A linha pega cada palavra e separa como um elemento da lista. A variável current_map recebe uma lista que foi convertida em string (usando join), após juntar os elementos da lista como um único (usando split)
                '''
                current_map = ' '.join(line.split(','))
                maps[current_map] = []  # Inicializa uma lista para cada tipo de mapa

            else:  # Adiciona linha do mapa no dicionário
                # print(list(line)) -> converte para lista
                maps[current_map].append(line)
    
        return maps[title]


def get_hyrule(size):
    points_map_hyrule.clear()  # Limpa a lista
    map = read_maps('# HYRULE')
    points_map = make_points(map, size)
    points_map_hyrule.append(points_map)

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0

    return Map(
        '# HYRULE',
        map_len,
        points_map[27][24],
        points_map[5][6],
        points_map,
        points_map[27][24],
    )


def get_dungeon1(size):
    map = read_maps('# DUNGEON 1')
    points_map = make_points(map, size)

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0
        
    return Map(
        '# DUNGEON 1',
        map_len,
        points_map[26][14],
        points_map[3][13],
        points_map,
        points_map_hyrule[0][1][24],
    )


def get_dungeon2(size):
    map = read_maps('# DUNGEON 2')
    points_map = make_points(map, size)

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0

    return Map(
        '# DUNGEON 2',
        map_len,
        points_map[25][13],
        points_map[2][13],
        points_map,
        points_map_hyrule[0][17][39],
    )


def get_dungeon3(size):
    map = read_maps('# DUNGEON 3')
    points_map = make_points(map, size)

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0

    return Map(
        '# DUNGEON 3',
        map_len,
        points_map[25][14],
        points_map[19][15],
        points_map,
        points_map_hyrule[0][32][5],
    )
