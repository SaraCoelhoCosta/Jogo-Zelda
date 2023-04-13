import pygame

POINTS = {
    'G': {'color': (113, 228, 57), 'cost': 10}, # LIGHT_GREEN (0, 255, 0)
    'D': {'color': (160, 140, 60), 'cost': 20}, # LIGHT_BROWN
    'F': {'color': (10, 102, 62), 'cost': 100}, # GREEN (0, 150, 50)
    'M': {'color': (113, 84, 27), 'cost': 150}, # BROWN (80, 40, 0)
    'R': {'color': (0, 150, 255), 'cost': 180}, # BLUE
    'C': {'color': (255, 255, 255), 'cost': 10}, # WHITE
    'B': {'color': (128, 128, 128), 'cost': 0}, # GREY
    'P': {'color': (255, 204, 229), 'cost': 0}, # TODO: Mudar ROSA
}
BLACK = (0, 0, 0) # Linhas


class Point: # Pontos do mapa
    def __init__(self, row, col, size, total_rows, point):
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.color = point['color']
        self.cost = point['cost']
        self.neighbors = []
        self.size = size
        self.total_rows = total_rows
        self.open = False

    def get_location(self):
        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.y, self.x, self.size, self.size))

    def is_barrier(self):
        return self.color == (128, 128, 128)  # TODO: refazer -- GREY
    
    def make_path(self):
        self.color = (128, 0, 128)  # TODO: refazer -- PURPLE

    def make_path2(self):
        self.color = (255, 0, 0)  # TODO: refazer -- RED

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # PARA BAIXO
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # PARA CIMA
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # PARA DIREITA
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # PARA ESQUERDA
            self.neighbors.append(grid[self.row][self.col - 1])


def make_points(map, size):  # Faz os pontos do mapa
    
    rows = len(map) # Conta quantos elementos tem na lista
    gap = size // rows # Quantidades de quadrados na janela
    win = []

    for i in range(rows):
        win.append([])
        for j in range(rows):
            point = Point(i, j, gap, rows, POINTS[map[i][j]]) # Cria o ponto
            win[i].append(point)

    return win


def draw_points(win, size_win, size_map, points_map): # Desenha os pontos do mapa
    for row in points_map:
        for point in row:
            point.draw(win)
    draw_line(win, size_win, size_map)
    pygame.display.update()


def draw_line(win, size_win, size_map):  # Desenha as linhas e colunas (divisões)
    gap = size_win // size_map 

    for i in range(size_map):
        pygame.draw.line(win, BLACK, (0, i * gap), (size_win, i * gap))
        for j in range(size_map):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, size_win))
