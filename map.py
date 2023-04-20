from points import create_points

maps = {}  # Variável global 

class Map: # Mapa
    def __init__(self, title, size, start, end, points_map, start_hyrule_1=None, start_hyrule_2=None, start_hyrule_3=None):
        self.title = title
        self.size = size
        self.start = start
        self.end = end
        self.points = points_map
        self.start_hyrule_1 = start_hyrule_1
        self.start_hyrule_2 = start_hyrule_2
        self.start_hyrule_3 = start_hyrule_3

    def map_size(self):
        return self.size

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
    map = read_maps('# HYRULE')
    map = create_points(map, size)
    maps['# HYRULE'] = map

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0

    return Map(
        '# HYRULE',
        map_len,
        map[27][24],
        map[5][6],
        map,
        map[1][24],
        map[17][39],
        map[32][5],
    )


def get_dungeon1(size):
    map = read_maps('# DUNGEON 1')
    map = create_points(map, size)
    maps['# DUNGEON 1'] = map

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0
        
    return Map(
        '# DUNGEON 1',
        map_len,
        map[26][14],
        map[3][13],
        map,
        maps['# HYRULE'][1][24],
    )


def get_dungeon2(size):
    map = read_maps('# DUNGEON 2')
    map = create_points(map, size)
    maps['# DUNGEON 2'] = map

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0

    return Map(
        '# DUNGEON 2',
        map_len,
        map[25][13],
        map[2][13],
        map,
        maps['# HYRULE'][17][39],
    )


def get_dungeon3(size):
    map = read_maps('# DUNGEON 3')
    map = create_points(map, size)
    maps['# DUNGEON 3'] = map

    if map is not None:
        map_len = len(map)
    else:
        map_len = 0

    return Map(
        '# DUNGEON 3',
        map_len,
        map[25][14],
        map[19][15],
        map,
        maps['# HYRULE'][32][5],
    )
