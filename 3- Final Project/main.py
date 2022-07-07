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
import EndOfGame
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
    saidaFloresta = Sprite("FlorestaSaida.png",1)
    saidaFloresta.x = janela.width/2+50
    saidaFloresta.y = janela.height-saidaFloresta.height-300
    
    cenarioCastelo = GameImage("Castelo.jpg")
    chaoCastelo = Sprite("CasteloChao.png",1)
    chaoCastelo.y = janela.height-chaoCastelo.height
    #saidaCastelo = Sprite("CasteloSaida.png",1)
    sangue = Sprite("sangue.png", 1)
    sangue.set_position(janela.width-sangue.width-10,janela.height-sangue.height-100)
    
    cenarioDungeon = GameImage("Dungeon.jpg")
    chaoDungeon = Sprite("DungeonChao.png",1) 
    chaoDungeon.y = janela.height-chaoDungeon.height
    
    cenario = 1
    
    # Instancio os objetos
    placa = Sprite("Placa.png",1)
    placa.x = janela.width/2 - 50
    placa.y = janela.height-placa.height-270
    
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
    vidasPlayer = vidas
    
    # Instancio o minotauro
    minotauro_Esq_Run = Sprite("MinotauroEsq.png", 8)
    minotauro_Esq_Run.x = janela.width-minotauro_Esq_Run.width
    minotauro_Esq_Run.y = janela.height-minotauro_Esq_Run.height
    minotauro_Esq_Run.set_total_duration(1000)
    
    minotauro_Dir_Run = Sprite("MinotauroDir.png", 8)
    minotauro_Dir_Run.x = janela.width-minotauro_Dir_Run.width
    minotauro_Dir_Run.y = janela.height-minotauro_Dir_Run.height
    minotauro_Dir_Run.set_total_duration(1000)
    
    minotauro_Esq = Sprite("Minotauro_Idle_Esq.png", 6)
    minotauro_Esq.x = janela.width-minotauro_Esq.width
    minotauro_Esq.y = janela.height-minotauro_Esq.height
    minotauro_Esq.set_total_duration(1000)

    minotauro_Dir = Sprite("Minotauro_Idle_Dir.png", 6)
    minotauro_Dir.x = janela.width-minotauro_Dir.width
    minotauro_Dir.y = janela.height-minotauro_Dir.height
    minotauro_Dir.set_total_duration(1000)

    minotauro_Death_Dir = Sprite("Minotauro_Death_Dir.png", 6)
    minotauro_Death_Dir.x = janela.width - minotauro_Death_Dir.width
    minotauro_Death_Dir.y = janela.height - minotauro_Death_Dir.height
    minotauro_Death_Dir.set_total_duration(1000)

    minotauro_Death_Esq = Sprite("Minotauro_Death_Esq.png", 6)
    minotauro_Death_Esq.x = janela.width-minotauro_Death_Esq.width
    minotauro_Death_Esq.y = janela.height-minotauro_Death_Esq.height
    minotauro_Death_Esq.set_total_duration(1000)

    minotauro_attack = Sprite("Minotauro_attack.png", 9) 
    minotauro_attack.x = janela.width - minotauro_attack.width
    minotauro_attack.y = janela.height - minotauro_attack.height
    minotauro_attack.set_total_duration(1000)

    minotauro_attack_Esq = Sprite("Minotauro_attack_Esq.png", 9)
    minotauro_attack_Esq.x = janela.width-minotauro_attack_Esq.width
    minotauro_attack_Esq.y = janela.height-minotauro_attack_Esq.height
    minotauro_attack_Esq.set_total_duration(1000)

    minotauro = minotauro_Esq
    vidasMinotauro = vidasInimigo
    
    # Instancio o cultista
    cultista_Esq_Run = Sprite("CultistaEsq.png", 10)
    cultista_Esq_Run.x = janela.width-minotauro_Esq_Run.width
    cultista_Esq_Run.y = janela.height-cultista_Esq_Run.height
    cultista_Esq_Run.set_total_duration(1000)
    
    cultista_Dir_Run = Sprite("CultistaDir.png", 10)
    cultista_Dir_Run.x = janela.width-minotauro_Dir_Run.width
    cultista_Dir_Run.y = janela.height-cultista_Dir_Run.height
    cultista_Dir_Run.set_total_duration(1000)
    
    cultista_Esq = Sprite("Cultista_Idle_Esq.png", 10)
    cultista_Esq.x = janela.width-minotauro_Esq.width
    cultista_Esq.y = janela.height-cultista_Esq.height
    cultista_Esq.set_total_duration(1000)

    cultista_Morte_Esq = Sprite("Cultista_Morte_Esq.png", 10)
    cultista_Morte_Esq.x = janela.width-cultista_Morte_Esq.width
    cultista_Morte_Esq.y = janela.height-cultista_Morte_Esq.height
    cultista_Morte_Esq.set_total_duration(1000)
    
    cultista_Dir = Sprite("Cultista_Idle_Dir.png", 10)
    cultista_Dir.x = janela.width-cultista_Dir.width
    cultista_Dir.y = janela.height-cultista_Dir.height
    cultista_Dir.set_total_duration(1000)
    
    cultista_Morte_Dir = Sprite("Cultista_Morte_Dir.png", 10)
    cultista_Morte_Dir.x = janela.width-cultista_Morte_Dir.width
    cultista_Morte_Dir.y = janela.height-cultista_Dir.height
    cultista_Morte_Dir.set_total_duration(1000)

    cultista = cultista_Esq
    vidasCultista = vidasInimigo
    
    # Instancio os guardas
    guardas_Esq_Run = Sprite("GuardasEsq.png", 6)
    guardas_Esq_Run.x = janela.width-guardas_Esq_Run.width
    guardas_Esq_Run.y = janela.height-guardas_Esq_Run.height
    guardas_Esq_Run.set_total_duration(1000)
    
    guardas_Dir_Run = Sprite("GuardasDir.png", 6)
    guardas_Dir_Run.x = janela.width-guardas_Dir_Run.width
    guardas_Dir_Run.y = janela.height-guardas_Dir_Run.height
    guardas_Dir_Run.set_total_duration(1000)
    
    guardas_Esq = Sprite("Guardas_Idle_Esq.png", 6)
    guardas_Esq.x = janela.width-guardas_Esq.width
    guardas_Esq.y = janela.height-guardas_Esq.height
    guardas_Esq.set_total_duration(1000)

    guardas_Morte_Esq = Sprite("Guardas_Morte_Esq.png", 6)
    guardas_Morte_Esq.x = janela.width-guardas_Morte_Esq.width
    guardas_Morte_Esq.y = janela.height-guardas_Morte_Esq.height
    guardas_Morte_Esq.set_total_duration(1000)

    guardas_Dir = Sprite("Guardas_Idle_Dir.png", 6)
    guardas_Dir.x = janela.width-guardas_Dir.width
    guardas_Dir.y = janela.height-guardas_Dir.height
    guardas_Dir.set_total_duration(1000)
    
    guardas_Morte_Dir = Sprite("Guardas_Morte_Dir.png", 6)
    guardas_Morte_Dir.x = janela.width-guardas_Morte_Dir.width
    guardas_Morte_Dir.y = janela.height-guardas_Morte_Dir.height
    guardas_Morte_Dir.set_total_duration(1000)
    
    guardas = guardas_Esq
    vidasGuardas = vidasInimigo
    
    # Instancio o Caebralum
    caebralum_Esq_Run = Sprite("CaebralumEsq.png", 5)
    caebralum_Esq_Run.x = janela.width-caebralum_Esq_Run.width
    caebralum_Esq_Run.y = janela.height-caebralum_Esq_Run.height
    caebralum_Esq_Run.set_total_duration(1000)
    
    caebralum_Dir_Run = Sprite("CaebralumDir.png", 5)
    caebralum_Dir_Run.x = janela.width-caebralum_Dir_Run.width
    caebralum_Dir_Run.y = janela.height-caebralum_Dir_Run.height
    caebralum_Dir_Run.set_total_duration(1000)
    
    caebralum_Esq = Sprite("Caebralum_Idle_Esq.png", 1)
    caebralum_Esq.x = janela.width-caebralum_Esq.width
    caebralum_Esq.y = janela.height-caebralum_Esq.height
    
    caebralum_Dir = Sprite("Caebralum_Idle_Dir.png", 1)
    caebralum_Dir.x = janela.width-caebralum_Dir.width
    caebralum_Dir.y = janela.height-caebralum_Dir.height
    
    caebralum = caebralum_Esq
    vidasCaebralum = vidasInimigo * 2
    
    # Crio o vetor de projeteis aliados e sua direçao
    listaProjeteisE = []
    listaProjeteisD = []
    checkPos=0

    # Crio o vetor de projeteis inimigos
    listaProjeteisInimigosE = []
    listaProjeteisInimigosD = []
    checkPosInim=0

    # Crio as variaveis dos inimigos
    summon = False
    spawn=0
    
    # Defino o frame per second
    FPS = 60
    clock = pygame.time.Clock()
    
    ################################################################################################################################
    ##################################################### Game Loop / Update() #####################################################
    ################################################################################################################################
    while(True):
        # Limito o Framerate
        clock.tick(FPS)
        
        # Desenho o cenario desejado e a placa que indica o que precisa ser feito
        if cenario==1:
            cenarioFloresta.draw()
            placa.draw()
            chao = chaoFloresta
            saida = saidaFloresta

            # Crio a movimentacao do minotauro
            checkPosInim = enemy.moveEnemy(janela,player,minotauro,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (minotauro.x<player.x and minotauro.x>0):
                    minotauro = enemy.SetEnemy(minotauro_Dir_Run,minotauro)
                    minotauro.update()

                #if (minotauro.x<= player.x and (minotauro.x-player.x)<120):
                #    minotauro = enemy.SetEnemy(minotauro_attack,minotauro)
                #    minotauro.update()

                if minotauro.x==player.x and minotauro.y == player.y:
                    minotauro = enemy.SetEnemy(minotauro_Dir,minotauro)
            else:
                if (minotauro.x>player.x and minotauro.x<janela.width):
                    minotauro = enemy.SetEnemy(minotauro_Esq_Run,minotauro)
                    minotauro.update()
                if minotauro.x==player.x and minotauro.y==player.y:
                    minotauro = enemy.SetEnemy(minotauro_Esq,minotauro)
            
            if ((player.collided(saida)) and vidasMinotauro<=0):
                cenario+=1
                player.set_position(0,janela.height/2+100)
                placa.set_position(janela.width/2-200,janela.height/2-100)
                summon=False
                
        elif cenario==2:
            cenarioCastelo.draw()
            sangue.draw()
            placa.draw()
            chao = chaoCastelo
            #saida = saidaCastelo
            
            # Crio a movimentacao do guarda
            checkPosInim = enemy.moveEnemy(janela,player,guardas,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (guardas.x<player.x and guardas.x>0):
                    guardas = enemy.SetEnemy(guardas_Dir_Run,guardas)
                    guardas.update()
                if guardas.x == player.x and guardas.y==player.y:
                    guardas = enemy.SetEnemy(guardas_Dir,guardas)
            else:
                if (guardas.x>player.x and minotauro.x<janela.width):
                    guardas = enemy.SetEnemy(guardas_Esq_Run,guardas)
                    guardas.update()
                if guardas.x == player.x and guardas.y==player.y:
                    guardas = enemy.SetEnemy(guardas_Esq,guardas)
        
            # Crio a movimentacao do cultista
            checkPosInim = enemy.moveEnemyRanged(janela,player,cultista,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (cultista.x<player.x and cultista.x>0):
                    cultista = enemy.SetEnemy(cultista_Dir_Run,cultista)
                    cultista.update()
                if cultista.x == player.x and cultista.y == player.y:
                    cultista = enemy.SetEnemy(cultista_Dir,cultista)
            else:
                if (cultista.x>player.x and cultista.x<janela.width):
                    cultista = enemy.SetEnemy(cultista_Esq_Run,cultista)
                    cultista.update()
                if cultista.x == player.x and cultista.y == player.y:
                    cultista = enemy.SetEnemy(cultista_Esq,cultista)
            
            if ((player.collided(sangue)) and (vidasCultista<=0 and vidasGuardas<=0)):
                cenario+=1
                player.x=0
                player.y=janela.height/2
        elif cenario==3:
            cenarioDungeon.draw()
            chao = chaoDungeon
            
            # Crio a movimentacao do Caebralum
            checkPosInim = enemy.moveEnemy(janela,player,caebralum,movimento,chao,checkPosInim)
            if checkPosInim==0:
                if (caebralum.x<player.x and caebralum.x>0):
                    caebralum = enemy.SetEnemy(caebralum_Dir_Run,caebralum)
                    caebralum.update()
                if caebralum.x == player.x and caebralum.y == player.y:
                    caebralum = enemy.SetEnemy(caebralum_Dir,caebralum)
            else:
                if (caebralum.x>player.x and caebralum.x<janela.width):
                    caebralum = enemy.SetEnemy(caebralum_Esq_Run,caebralum)
                    caebralum.update()
                if caebralum.x == player.x and caebralum.y == player.y:
                    caebralum = enemy.SetEnemy(caebralum_Esq,caebralum)
        
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
        
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            mixer.music.stop()
            menu.menu()
        
        # Chamo a funçao que lidará com o desenho da barra de vida
        life(vidas,movimentoInimigo)
            
        # Chamo a funçao que irá lidar com a criaçao dos tiros
        if (teclado.key_pressed("SPACE") and delay==0):
            Player.criaProjetil(player,listaProjeteisE,listaProjeteisD,checkPos)
            delay = shooting.recarga(movimentoInimigo,delay)
        if (delayInimigo==0):
            delayInimigo = shooting.recargaCultistaInimigo(movimentoInimigo,delayInimigo)
            
        # Faço o movimento dos tiros
        Player.magicAttack(janela,listaProjeteisE,listaProjeteisD,velProjetil)
        enemy.magicAttackInimigo(janela,listaProjeteisE,listaProjeteisD,velProjetil)
        if delay>0:
            delay-=1
        if delayInimigo>0:
            delayInimigo-=1
        
        # Desenho o personagem principal
        if vidasPlayer>0:
            player.draw()
        else:
            EndOfGame.derrota()
        
        # Checo se tomei dano
        vidasPlayer = Player.hit(listaProjeteisInimigosE,listaProjeteisInimigosD,player,vidasPlayer)
        
        # Desenho as instruçoes
        if player.collided(placa) and cenario==1:
            janela.draw_text(("DERROTE o MINOTAURO PARA PROSSEGUIR!"), (janela.width/2)-325, 20, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
            summon = True
            if spawn==0:
                minotauro.set_position(janela.width-minotauro.width,(janela.height/2)-(minotauro.height/2))
                spawn+=1
        elif player.collided(placa) and cenario==2:
            janela.draw_text(("SIGA O RASTRO DE SANGUE ATÉ O CALABOUÇO!"), (janela.width/2)-325, 20, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
            summon = True
            if spawn==1:
                cultista.set_position(janela.width-cultista.width,janela.height-cultista.height)
                guardas.set_position(janela.width-guardas.width,0)
                spawn+=1
        
        # Desenho os monstros
        if cenario==1 and (summon==True):
            if (vidasMinotauro>0):
                minotauro.draw()
                vidasMinotauro = enemy.hitFloresta(listaProjeteisE,listaProjeteisD,minotauro,vidasMinotauro)
        
        if cenario==2 and (summon==True):
            if (vidasCultista>0):
                cultista.draw()
                vidasCultista = enemy.hitCasteloCultista(listaProjeteisE,listaProjeteisD,cultista,vidasCultista)
            if (vidasGuardas>0):
                guardas.draw()
                vidasGuardas = enemy.hitCasteloGuardas(listaProjeteisE,listaProjeteisD,guardas,vidasGuardas)
        if cenario==3 and (summon==True):
            if (vidasCaebralum>0):
                caebralum.draw()
                vidasCaebralum = enemy.hitDungeon(listaProjeteisE,listaProjeteisD,caebralum,vidasCaebralum)
        
        # Termino o jogo se mato o boss final
        if vidasCaebralum<=0:
            EndOfGame.vitoria()

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()

def life(vidas,movimentoInimigo):
    # Instancio as barras de vida
    healthBarFull = Sprite("HealthBarFull.png", 1)
    healthBarFull.set_position(0,0)
    
    healthBarMedium1 = Sprite("HealthBarMedium1.png", 1)
    healthBarMedium1.set_position(0,0)
    
    healthBarMedium2 = Sprite("HealthBarMedium2.png", 1)
    healthBarMedium2.set_position(0,0)

    healthBarMedium3 = Sprite("HealthBarMedium3.png", 1)
    healthBarMedium3.set_position(0,0)

    healthBarLow = Sprite("HealthBarLow.png", 1)
    healthBarLow.set_position(0,0)
        
    # Desenho a barra de vida desejada
    if abs(movimentoInimigo)==150:
        if (vidas==3):
            healthBarFull.draw()
        if (vidas==2):
            healthBarMedium2.draw()
        if (vidas==1):
            healthBarLow.draw()
    else:
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