import pygame
from queue import PriorityQueue

SIZE = 672 # Tamanho da janela
WINDOW = pygame.display.set_mode((SIZE, SIZE))  # Tamanho da janela
pygame.display.set_caption('Zelda com A*')  # Título

POINTS = {
    'G': {'color': (0, 255, 0), 'cost': 10}, # LIGHT_GREEN
    'D': {'color': (160, 140, 60), 'cost': 20}, # LIGHT_BROWN
    'F': {'color': (0, 150, 50), 'cost': 100}, # GREEN
    'M': {'color': (80, 40, 0), 'cost': 150}, # BROWN
    'R': {'color': (0, 150, 255), 'cost': 180}, # BLUE
    'C': {'color': (255, 255, 255), 'cost': 10}, # WHITE
    'B': {'color': (128, 128, 128), 'cost': 0}, # GREY
}

BLACK = (0, 0, 0) # Linhas

class Point: # PONTOS 
    def __init__(self, row, col, size, total_rows, color, cost, t):
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.color = color
        self.cost = cost
        self.neighbors = []
        self.size = size  # TODO: tamanho?
        self.total_rows = total_rows
        self.t = t

    def get_location(self):
        return self.row, self.col
    
    def get_type(self):
        return self.t

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.y, self.x, self.size, self.size))


def read_maps():
    with open("maps.txt", "r") as file:  # Lê o arquivo de texto com os mapas
        lines = file.readlines()

    maps = {}

    for line in lines:
        line = line.split('\n')[0]

        if not (line.strip()):  # Ignora linha vazia
            continue

        elif line[0] == '#':  # Verifica se a linha é igual ao título do mapa
            '''
                A linha pega cada palavra e separa como um elemento da lista. A variável current_map recebe uma lista que foi convertida em string (usando join), após juntar os elementos da lista como um único (usando split)
            '''
            current_map = ' '.join(line.split(','))
            maps[current_map] = []  # Inicializa a lista de linhas do mapa

        else:  # Adiciona linha do mapa no dicionário
            # print(list(line)) -> converte para lista
            maps[current_map].append(line)
    return maps


def make_grid(maps=read_maps(), title='# HYRULE', size=SIZE):  # Desenha os pontos do mapa
    
    grid = maps[title] # Recebe um mapa
    rows = len(grid) # Conta quantos elementos tem na lista
    gap = size // rows # Quantidades de quadrados na janela
    win = []

    for i in range(rows): # Varre o mapa
        for j in range(rows):
            point = Point(i, j, gap, rows, POINTS[grid[i][j]]['color'], POINTS[grid[i][j]]['cost'], grid[i][j]) # Cria o ponto
            win.append(point)
    return win


def draw_grid(win, rows, size):  # Desenha as linhas e colunas
    gap = size // rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (size, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, size))


def draw(win, grid, rows, size):
    for row in grid:
        #for point in row:
        row.draw(win)
    draw_grid(win, rows, size)
    pygame.display.update()


grid = make_grid()
run = True
while run:
    draw(WINDOW, grid, 42, SIZE)
