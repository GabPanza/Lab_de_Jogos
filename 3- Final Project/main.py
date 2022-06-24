from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*
from PPlay.mouse import*
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

def game(vidas,vidasInimigo,movimento,movimentoInimigo,velProjetil,velProjetilInimigo,delay,delayInimigo):
    # Instancio o tamanho da janela
    janela = Window(1280,720)

    # Inicializo o teclado
    teclado = janela.get_keyboard()

    # Adiciono musica
    mixer.music.load("EnvironmentMusic.wav")
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    
    # Instancio os cenários
    cenarioFloresta = GameImage("Floresta.jpg")
    chaoFloresta = Sprite("FlorestaChao.png",1)
    chaoFloresta.y = janela.height-chaoFloresta.height
    
    cenarioFloresta2 = GameImage("Floresta2.jpg")
    chaoFloresta2 = Sprite("FlorestaChao2.png",1)
    chaoFloresta2.y = janela.height-chaoFloresta2.height
    
    cenarioCastelo = GameImage("Castelo.jpg")
    chaoCastelo = Sprite("CasteloChao.png",1)
    chaoCastelo.y = janela.height-chaoCastelo.height

    cenarioCastelo2 = GameImage("Castelo2.jpg")
    chaoCastelo2 = Sprite("CasteloChao2.png",1)
    chaoCastelo2.y = janela.height-chaoCastelo2.height
    
    cenarioDungeon = GameImage("Dungeon.jpg")
    chaoDungeon = Sprite("DungeonChao.png",1) 
    chaoDungeon.y = janela.height-chaoDungeon.height
    
    cenario = 1
    chao = chaoFloresta
    
    # Instancio os objetos
    placa = Sprite("Placa.png",1)
    placa.x = janela.width - placa.width - 50
    placa.y = janela.height-placa.height-240    
    plataforma = GameImage("Plataforma.jpg")
    
    # Instancio a Emih
    player_Esq_Run = Sprite("Emih_invertido.png", 8)
    player_Esq_Run.x = 0
    player_Esq_Run.y = janela.height-player_Esq_Run.height
    player_Esq_Run.set_total_duration(1000)
    
    player_Dir_Run = Sprite("Emih.png", 8)
    player_Dir_Run.x = 0
    player_Dir_Run.y = janela.height-player_Dir_Run.height
    player_Dir_Run.set_total_duration(1000)
    
    player_Esq = Sprite("Emih_invertido_Idle.png", 1)
    player_Esq.x = 0
    player_Esq.y = janela.height-player_Esq.height
    
    player_Dir = Sprite("Emih_Idle.png", 1)
    player_Dir.x = 0
    player_Dir.y = janela.height-player_Dir.height
    
    player = player_Dir
    
    # Instancio o Caebralum
    caebralum_Esq_Run = Sprite("CaebralumEsq.png", 8)
    caebralum_Esq_Run.x = 0
    caebralum_Esq_Run.y = janela.height-caebralum_Esq_Run.height
    caebralum_Esq_Run.set_total_duration(1000)
    
    caebralum_Dir_Run = Sprite("CaebralumDir.png", 8)
    caebralum_Dir_Run.x = 0
    caebralum_Dir_Run.y = janela.height-caebralum_Dir_Run.height
    caebralum_Dir_Run.set_total_duration(1000)
    
    caebralum_Esq = Sprite("Caebralum_Idle_Esq.png", 1)
    caebralum_Esq.x = 0
    caebralum_Esq.y = janela.height-caebralum_Esq.height
    
    caebralum_Dir = Sprite("Caebralum_Idle_Dir.png", 1)
    caebralum_Dir.x = 0
    caebralum_Dir.y = janela.height-caebralum_Dir.height
    
    caebralum = caebralum_Esq
    
    # Instancio o minotauro
    minotauro_Esq_Run = Sprite("CaebralumEsq.png", 5)
    minotauro_Esq_Run.x = 0
    minotauro_Esq_Run.y = janela.height-minotauro_Esq_Run.height
    minotauro_Esq_Run.set_total_duration(1000)
    
    minotauro_Dir_Run = Sprite("CaebralumDir.png", 5)
    minotauro_Dir_Run.x = 0
    minotauro_Dir_Run.y = janela.height-minotauro_Dir_Run.height
    minotauro_Dir_Run.set_total_duration(1000)
    
    minotauro_Esq = Sprite("Caebralum_Idle_Esq.png", 1)
    minotauro_Esq.x = 0
    minotauro_Esq.y = janela.height-minotauro_Esq.height
    
    minotauro_Dir = Sprite("Caebralum_Idle_Dir.png", 1)
    minotauro_Dir.x = 0
    minotauro_Dir.y = janela.height-minotauro_Dir.height
    
    minotauro = minotauro_Dir
    
    # Instancio o cultista
    cultista_Esq_Run = Sprite("CultistaEsq.png", 10)
    cultista_Esq_Run.x = 0
    cultista_Esq_Run.y = janela.height-cultista_Esq_Run.height
    cultista_Esq_Run.set_total_duration(1000)
    
    cultista_Dir_Run = Sprite("CultistaDir.png", 10)
    cultista_Dir_Run.x = 0
    cultista_Dir_Run.y = janela.height-cultista_Dir_Run.height
    cultista_Dir_Run.set_total_duration(1000)
    
    cultista_Esq = Sprite("Cultista_Idle_Esq.png", 10)
    cultista_Esq.x = 0
    cultista_Esq.y = janela.height-cultista_Esq.height
    cultista_Esq.set_total_duration(1000)

    cultista_Morte_Esq = Sprite("Cultista_Morte_Esq.png", 10)
    cultista_Morte_Esq.x = 0
    cultista_Morte_Esq.y = janela.height-cultista_Morte_Esq.height
    cultista_Morte_Esq.set_total_duration(1000)
    
    cultista_Dir = Sprite("Cultista_Idle_Dir.png", 10)
    cultista_Dir.x = 0
    cultista_Dir.y = janela.height-cultista_Dir.height
    cultista_Dir.set_total_duration(1000)
    
    cultista_Morte_Dir = Sprite("Cultista_Morte_Dir.png", 10)
    cultista_Morte_Dir.x = 0
    cultista_Morte_Dir.y = janela.height-cultista_Dir.height
    cultista_Morte_Dir.set_total_duration(1000)

    cultista = cultista_Esq
    
    # Instancio os guardas
    guardas_Esq_Run = Sprite("GuardasEsq.png", 6)
    guardas_Esq_Run.x = 0
    guardas_Esq_Run.y = janela.height-guardas_Esq_Run.height
    guardas_Esq_Run.set_total_duration(1000)
    
    guardas_Dir_Run = Sprite("GuardasDir.png", 6)
    guardas_Dir_Run.x = 0
    guardas_Dir_Run.y = janela.height-guardas_Dir_Run.height
    guardas_Dir_Run.set_total_duration(1000)
    
    guardas_Esq = Sprite("Guardas_Idle_Esq.png", 6)
    guardas_Esq.x = 0
    guardas_Esq.y = janela.height-guardas_Esq.height
    guardas_Esq.set_total_duration(1000)

    guardas_Morte_Esq = Sprite("Guardas_Morte_Esq.png", 6)
    guardas_Morte_Esq.x = 0
    guardas_Morte_Esq.y = janela.height-guardas_Morte_Esq.height
    guardas_Morte_Esq.set_total_duration(1000)

    guardas_Dir = Sprite("Guardas_Idle_Dir.png", 6)
    guardas_Dir.x = 0
    guardas_Dir.y = janela.height-guardas_Dir.height
    guardas_Dir.set_total_duration(1000)
    
    guardas_Morte_Dir = Sprite("Guardas_Morte_Dir.png", 6)
    guardas_Morte_Dir.x = 0
    guardas_Morte_Dir.y = janela.height-guardas_Morte_Dir.height
    guardas_Morte_Dir.set_total_duration(1000)
    
    guardas = guardas_Esq
    
    # Crio o vetor de projeteis aliados e sua direçao
    listaProjeteisE = []
    listaProjeteisD = []
    checkPos=0
    
    # Crio o vetor de projeteis inimigos
    listaProjeteisInimigosE = []
    listaProjeteisInimigosD = []
    checkPosInim=0
    
    # Crio a lista de inimigos
    listaInimigos = []
    
    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()
    
    ################################################################################################################################
    ##################################################### Game Loop / Update() #####################################################
    ################################################################################################################################
    while(True):
        # Defino o Framerate
        clock.tick(FPS)
        
        # Desenho o cenario desejado e a placa que indica o que precisa ser feito
        if cenario==1:
            cenarioFloresta.draw()
            placa.draw()
            # Crio a movimentacao do minotauro
            checkPosInim = enemy.moveEnemy(janela,player,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (minotauro.x>player.x and minotauro.x<janela.width):
                    minotauro = enemy.SetEnemy(minotauro_Dir_Run,minotauro)
                    minotauro.update()
                if not player:
                    minotauro = enemy.SetEnemy(minotauro_Dir,minotauro)
            elif checkPosInim==1:
                if (minotauro.x<player.x and minotauro.x>0):
                    minotauro = enemy.SetEnemy(minotauro_Esq_Run,minotauro)
                    minotauro.update()
                if not player:
                    minotauro = enemy.SetEnemy(minotauro_Esq,minotauro)
        
        elif cenario==2:
            cenarioFloresta2.draw()
            placa.draw()
        
        elif cenario==3:
            cenarioCastelo.draw()
            placa.draw()
            # Crio a movimentacao do guarda
            checkPosInim = enemy.moveEnemy(janela,player,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (guardas.x>player.x and guardas.x<janela.width):
                    guardas = enemy.SetEnemy(guardas_Dir_Run,guardas)
                    guardas.update()
                if not player:
                    guardas = enemy.SetEnemy(guardas_Dir,guardas)
            elif checkPosInim==1:
                if (guardas.x<player.x and guardas.x>0):
                    guardas = enemy.SetEnemy(guardas_Esq_Run,guardas)
                    guardas.update()
                if not player:
                    guardas = enemy.SetEnemy(guardas_Esq,guardas)
        
        elif cenario==4:
            cenarioCastelo2.draw()
            placa.draw()
            # Crio a movimentacao do cultista
            checkPosInim = enemy.moveEnemy(janela,player,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (cultista.x>player.x and cultista.x<janela.width):
                    cultista = enemy.SetEnemy(cultista_Dir_Run,cultista)
                    cultista.update()
                if not player:
                    cultista = enemy.SetEnemy(cultista_Dir,cultista)
            elif checkPosInim==1:
                if (cultista.x<player.x and cultista.x>0):
                    cultista = enemy.SetEnemy(cultista_Esq_Run,cultista)
                    cultista.update()
                if not player:
                    cultista = enemy.SetEnemy(cultista_Esq,cultista)
        
        elif cenario==5:
            cenarioDungeon.draw()
            # Crio a movimentacao do Caebralum
            checkPosInim = enemy.moveEnemy(janela,player,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (caebralum.x>player.x and caebralum.x<janela.width):
                    caebralum = enemy.SetEnemy(caebralum_Dir_Run,caebralum)
                    caebralum.update()
                if not player:
                    caebralum = enemy.SetEnemy(caebralum_Dir,caebralum)
            elif checkPosInim==1:
                if (caebralum.x<player.x and caebralum.x>0):
                    caebralum = enemy.SetEnemy(caebralum_Esq_Run,caebralum)
                    caebralum.update()
                if not player:
                    caebralum = enemy.SetEnemy(caebralum_Esq,caebralum)
        
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            mixer.music.stop()
            menu.menu()
        
        # Chamo a funçao que lidará com o desenho da barra de vida
        life(vidas)
        
        # Crio a movimentacao do personagem principal
        checkPos = Player.movePlayer(janela,teclado,player,movimento,chao,checkPos)
        if checkPos==0:
            if (teclado.key_pressed("D") or teclado.key_pressed("RIGHT")):
                player = Player.SetPlayer(player_Dir_Run,player)
                player.update()
            else:
                player = Player.SetPlayer(player_Dir,player)
        elif checkPos==1:
            if (teclado.key_pressed("A") or teclado.key_pressed("LEFT")):
                player = Player.SetPlayer(player_Esq_Run,player)
                player.update()
            else:
                player = Player.SetPlayer(player_Esq,player)
        
        # Crio a condiçao para mudar de cenário
        if ((player.x>janela.width-player.width/2) and (len(listaInimigos) == 0)):
            cenario+=1
        
        # Chamo a funçao que irá lidar com a criaçao dos tiros
        if (teclado.key_pressed("SPACE") and delay==0):
            Player.criaProjetil(player,listaProjeteisE,listaProjeteisD,checkPos)
            delay = shooting.recarga(movimentoInimigo,delay)
            
        # Faço o movimento dos tiros
        Player.magicAttack(janela,listaProjeteisE,listaProjeteisD,velProjetil,checkPos)
        if delay>0:
            delay-=1
        if delayInimigo>0:
            delayInimigo-=1
        
        # Desenho o personagem principal
        player.draw()
        
        # Desenho as instruçoes
        if player.collided(placa) and cenario==1:
            janela.draw_text(("DERROTE TODOS OS INIMIGOS PARA PROSSEGUIR!"), (janela.width/2)-325, 20, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        
        if player.collided(placa) and cenario==2:
            janela.draw_text(("SIGA OS CULTISTAS ATÉ O CASTELO!"), (janela.width/2)-325, 20, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        
        if player.collided(placa) and cenario==3:
            janela.draw_text(("DERROTE TODOS OS INIMIGOS PARA PROSSEGUIR!"), (janela.width/2)-325, 20, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        
        if player.collided(placa) and cenario==4:
            janela.draw_text(("SIGA OS CULTISTAS ATÉ O CALABOUÇO!"), (janela.width/2)-325, 20, size=28, font_name="Arial", bold=True,color=[255, 255, 0])

        # Desenho o fps
        janela.draw_text(str(clock), janela.width-200, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()

def life(vidas):
    # Instancio as barras de vida
    healthBarFull = Sprite("HealthBarFull.png", 1)
    healthBarMedium1 = Sprite("HealthBarMedium1.png", 1)
    healthBarMedium2 = Sprite("HealthBarMedium2.png", 1)
    healthBarMedium3 = Sprite("HealthBarMedium3.png", 1)
    healthBarLow = Sprite("HealthBarLow.png", 1)
    # Defino a posiçao das imagens de Vida
    healthBarFull.set_position(0,0)
    healthBarMedium1.set_position(0,0)
    healthBarMedium2.set_position(0,0)
    healthBarMedium3.set_position(0,0)
    healthBarLow.set_position(0,0)
    # Desenho a barra de vida desejada
    if (vidas==5):
        healthBarFull.draw()
    if (vidas==4):
        healthBarMedium1.draw()
    if (vidas==3):
        healthBarMedium2.draw()
    if (vidas==2):
        healthBarMedium3.draw()
    if (vidas==1):
        healthBarLow.draw()