class Game:
    ''' 
        TODO: 
            1. Por qual mapa começar
            2. Transição de mapas
            3. Pegar pingentes 
            4. Retornar
            5. Transição de mapas
            6. Próximo mapa (2)
            7. Pegar espada
            8. Ir para o final
    '''
    def best_way():
        pass


# Classe que representa um item do jogo
class Item:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.collected = False
