from points import create_points

maps = {}  # Variável global 

class Map: # Mapa
    # Construtor recebe todos os parâmetros necessários para criar o mapa
    def __init__(self, title, size, start, end, points_map, start_hyrule_1=None, start_hyrule_2=None, start_hyrule_3=None):
        self.title = title
        self.size = size
        self.start = start
        self.end = end
        self.points = points_map
        self.start_hyrule_1 = start_hyrule_1
        self.start_hyrule_2 = start_hyrule_2
        self.start_hyrule_3 = start_hyrule_3

    # Função que retorna o tamanho do mapa
    def map_size(self):
        return self.size

# Função que lê cada um dos mapas
def read_maps(title):
    current_map = '' # Variável inicializada, que simboliza a chave do mapa, com uma string vazia, para posteriormente receber na lista os títulos dos mapas

    if len(maps) != 0:  # Se o tamamnho do mapa for diferente de 0, significa que o mapa já foi lido e sua leitura não será feita novamente
        return maps[title]
    
    elif len(maps) == 0: # Se o tamanho for vazio
        with open("maps.txt", "r") as file:  # O arquivo .txt com os mapas é aberto e é feita a leitura deles
            lines = file.readlines() # Variável que recebe tudo o que foi lido no arquivo

        for line in lines: # Adiciona-se um \n ao final de cada linha, ao se encontrar um enter
            line = line.split('\n')[0]

            if not (line.strip()):  # Ignora linha vazia
                continue

            elif line[0] == '#':  # Verifica se a linha é igual ao título do mapa
                '''
                    A linha pega cada palavra e separa como um elemento da lista. 
                    A variável current_map recebe uma lista que foi convertida em string (usando join), 
                    após juntar os elementos da lista como um único (usando split)
                '''
                current_map = ' '.join(line.split(',')) # Pega o título de cada mapa e separa por vírgulas numa lista
                maps[current_map] = []  # Inicializa uma lista para cada tipo de mapa

            else:  # Adiciona linha do mapa no dicionário
                # print(list(line)) -> converte para lista
                maps[current_map].append(line) # Cria a lista de strings do mapa a ser lido, a fim de não ler novamente
    
        return maps[title] # Retorna o mapa que foi lido
    
# Função que retorna o mapa principal
def get_hyrule(size):

    map = read_maps('# HYRULE')
    map = create_points(map, size)
    maps['# HYRULE'] = map

    if map is not None: # Se o mapa já tiver algum valor, a variável de tamanho do mapa é inicializada com o tamanho dele
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

# Função que retorna a primeira dungeon a ser percorrida
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

# Função que retorna a segunda dungeon a ser percorrida
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

# Função que retorna a terceira dungeon a ser percorrida
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
