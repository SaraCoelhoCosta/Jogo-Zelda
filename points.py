import pygame

POINTS = {
    'G': {'cost': 10, 'texture': './textures/grass.png'}, # LIGHT_GREEN
    'D': {'cost': 20, 'texture': './textures/desert.png'}, # LIGHT_BROWN
    'F': {'cost': 100, 'texture': './textures/grass.png' , 'object': './textures/trees/tree.png'}, # GREEN
    'M': {'cost': 150, 'texture': './textures/dirt.png'}, # BROWN
    'R': {'cost': 180, 'texture': './textures/water.png'}, # BLUE
    'C': {'cost': 10, 'texture': './textures/floor.png'}, # WHITE
    'B': {'cost': 0, 'texture': './textures/wall.png'}, # GREY
}

class Point: # Pontos do mapa
    def __init__(self, row, col, size, total_rows, point):
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.cost = point['cost']
        self.neighbors = []
        self.size = size
        self.total_rows = total_rows
        self.open = False
        self.texture = pygame.transform.scale(pygame.image.load(point['texture']), (size, size))
        
        if 'object' in point:
            self.object = pygame.image.load(point['object'])
            self.object = pygame.transform.scale(self.object, (size, size))

    def get_location(self):
        return [self.row, self.col]

    def draw(self, win):
        if hasattr(self, 'object'):
            win.blit(self.texture, (self.y, self.x))
            win.blit(self.object, (self.y, self.x))
        elif hasattr(self, 'texture'):
            win.blit(self.texture, (self.y, self.x))

        # if ((self.row == 1 and self.col == 24) or (self.row == 17 and self.col == 39) or (self.row == 32 and self.col == 5)) and self.total_rows == 42:
        #    win.blit(pygame.transform.scale(pygame.image.load('./textures/portal/portal_7.png'), (self.size, self.size)), (self.col * self.size, self.row * self.size))

    def is_barrier(self):
        return self.cost == 0

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


def create_points(map, size):  # Faz os pontos do mapa
    
    rows = len(map) # Conta quantos elementos tem na lista
    gap = size // rows # Quantidades de quadrados na janela
    win = []

    for i in range(rows):
        win.append([])
        for j in range(rows):
            point = Point(i, j, gap, rows, POINTS[map[i][j]]) # Cria o ponto
            win[i].append(point)

    return win
