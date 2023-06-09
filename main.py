import sys
import pygame
from draw_map import draw_points
from game import play
from map import get_hyrule

SIZE = 672 # Tamanho da janela
WINDOW = pygame.display.set_mode((SIZE, SIZE))  # Tamanho da janela
SECOND_WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Zelda com A*')  # Título

def main(win=WINDOW, second_win=SECOND_WINDOW, size_win=SIZE):
    hyrule = get_hyrule(size_win)

    run = True # Permite que o jogo continue rodando
    start_play = False # Controla se o jogo foi iniciado
    end = False # Controla se o jogo foi finalizado
    while run:
        draw_points(win, size_win, hyrule.size, hyrule.points, hyrule, end)
        
        if not start_play: # Mostra personagem na tela enquanto não inicia
            win.blit(pygame.transform.scale(pygame.image.load('./sprites/link/link_f1.png'), (hyrule.points[0][0].size, hyrule.points[0][0].size)), (hyrule.start.get_location()[1] * hyrule.points[0][0].size, hyrule.start.get_location()[0] * hyrule.points[0][0].size))
            pygame.display.update()
        
        if end: # Se end recebe TRUE, ou seja, Link chegou ao nó objetivo, é exibida a sua imagem com a espada
            win.blit(pygame.transform.scale(pygame.image.load('./sprites/link/link.png'), (hyrule.points[0][0].size, hyrule.points[0][0].size)), (hyrule.points[1][2].get_location()[1] * hyrule.points[0][0].size, hyrule.points[1][2].get_location()[0] * hyrule.points[0][0].size))
            pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT: # Fecha a janela e encerra programa com o botão X
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: # Fecha a janela e encerrar programa com o Q
                    run = False
                    pygame.quit()
                    sys.exit()
                '''
                if event.key == pygame.K_c and start_play: # Limpa o mapa
                    start_play = False
                    hyrule = get_hyrule(size_win)
                ''' 

                if event.key == pygame.K_SPACE and not start_play: # Roda o jogo
                    start_play = True
                    pygame.mixer.init()
                    pygame.mixer.music.load("./music/fundo_musical.mp3")
                    pygame.mixer.music.play()
                    play(win, second_win, size_win, hyrule) # Chamada da função play
                    end = True

if __name__ == '__main__':
    main()
