from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*
import menu
import Player 
import enemy
import shooting
import pygame
from pygame import mixer

################################################################################################################################
################################################ Inicializações / Start() ######################################################
################################################################################################################################
def game(vidas,movimento,movimentoInimigo,velProjetil,velProjetilInimigo,delay,delayInimigo,linha):
    # Instancio o tamanho da janela
    janela = Window(1280,720)

    # Instancio o teclado
    teclado = janela.get_keyboard()

    # Instancio os objetos do jogo
    espaco = GameImage("espaço.jpg")
    player = Sprite("nave.png",1)
    
    # Defino a posiçao do player
    player.x = janela.width/2
    player.y = janela.height - player.height - 20
    
    # Instancio o som do jogo
    mixer.music.load("Megalovania.wav")
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    
    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()

    # Crio o vetor de projeteis inimigos
    listaProjeteisInimigos = []
    listaProjeteis = []
    listaProjeteisNavemae = []
    
    # Crio o vetor de inimigos
    matrizDeInimigos = []
    spawnNaveMae = 600
    
    # Crio a pontuaçao que os aliens dão
    score = 0
    
    ################################################################################################################################
    ################################################ Gameloop / Update() ###########################################################
    ################################################################################################################################
    while (True):
        # Desenho o fundo
        espaco.draw()
                
        # Conto o fps
        clock.tick(FPS)
    
        # Volto pro menu do jogo
        if (teclado.key_pressed("ESC")):
            mixer.music.stop()
            menu.MainMenu()
            
        # Faço a movimentação do personagem
        Player.player(janela,teclado,player,movimento)
        
        # Crio os inimigos
        if (len(matrizDeInimigos)==0):
            enemy.spawn(linha,matrizDeInimigos)

        # Recrio a matriz apos matar todos os aliens
        for i in matrizDeInimigos:
            if (len(i)==0):
                vazio = True
            else:
                vazio = False
                break
        if vazio:    
            matrizDeInimigos.clear()
            linha+=1
            if linha==6:
                naveMae = enemy.spawn(linha,matrizDeInimigos)
            else:
                enemy.spawn(linha,matrizDeInimigos)
            if (score==2880):
                mixer.music.stop()
                import ranking
                ranking.fimDoJogoVitoria(score)
            if (score==3360 or score==3460):
                mixer.music.stop()
                import ranking
                ranking.fimDoJogoVitoria(score)
        
        # Faço o movimento dos inimigos
        movimentoInimigo = enemy.moveInimigos(janela, matrizDeInimigos, movimentoInimigo)
        
        # Faço o movimento da nave mae
        if linha==6:
            if spawnNaveMae>0:
                spawnNaveMae-=1
            else:
                if naveMae.y>0:
                    naveMae.draw()
                    naveMae.x += 100*janela.delta_time()
                    shooting.criaProjNaveMae(naveMae,listaProjeteisNavemae)
                    score = enemy.killNavemae(listaProjeteis,score,naveMae)

        # Chamo a funçao que irá lidar com a criaçao dos tiros
        if (teclado.key_pressed("SPACE") and delay==0):
            shooting.criaProjNave(player,listaProjeteis)
            delay = shooting.delay(movimentoInimigo,delay)
        if (delayInimigo==0):
            for i in matrizDeInimigos:
                for j in i:
                    shooting.criaProjInimigo(j,listaProjeteisInimigos)
            delayInimigo = shooting.delayInimigo(movimentoInimigo,delayInimigo)
            
        # Faço o movimento dos tiros
        shooting.tiroPlayer(janela,listaProjeteis,velProjetil)
        shooting.tiroInimigo(janela,listaProjeteisInimigos,velProjetilInimigo)
        shooting.tiroNaveMae(janela,listaProjeteisNavemae,velProjetilInimigo)
        if delay>0:
            delay-=1
        if delayInimigo>0:
            delayInimigo-=1
        
        # Verifico se alguem tomou hit
        score = enemy.kill(listaProjeteis,matrizDeInimigos,score,linha)
        if (vidas>0):
            for i in matrizDeInimigos:
                vidas = enemy.hit(vidas, player, i, listaProjeteisInimigos,listaProjeteisNavemae,score)
        
        # Desenho os objetos
        player.draw()
        enemy.draw(matrizDeInimigos)
        
        # Desenho a dificuldade do jogo
        if (movimentoInimigo==100 or movimentoInimigo==-100):
            janela.draw_text(("Difficult: Easy"), 0, 0, size=24, font_name="Arial", bold=True,color=[0, 255, 0])
        if (movimentoInimigo==120 or movimentoInimigo==-120):
            janela.draw_text(("Difficult: Medium"), 0, 0, size=24, font_name="Arial", bold=True,color=[255, 255, 0])
        if (movimentoInimigo==150 or movimentoInimigo==-150):
            janela.draw_text(("Difficult: Hard"), 0, 0, size=24, font_name="Arial", bold=True,color=[255, 0, 0])
        
        # Perco o jogo
        if (vidas <= 0):
            mixer.music.stop()
            import ranking
            ranking.fimDoJogoDerrota(score) 
            
        # Desenho o fps
        janela.draw_text(str(clock), janela.width-200, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Desenho a pontuação
        janela.draw_text(("Score: "), janela.width-130, 25, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score), janela.width-50, 25, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Desenho a vida
        janela.draw_text(("Vidas: "), 0, 25, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(vidas), 75, 25, size=24, font_name="Arial", bold=True,color=[255, 0, 0])

        # Instancio o titulo da janela  
        janela.set_title("Space Invaders")
        
        # Finalizo o Gameloop
        janela.update()