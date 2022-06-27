from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*

def SetEnemy(EnemyState,EnemyAtual):
    Enemy = EnemyState
    Enemy.x = EnemyAtual.x
    Enemy.y = EnemyAtual.y
    return Enemy

def drawMonstros(minotauro,guardas,cultista,caebralum,cenario):
    if cenario==1:
        minotauro.draw()
    if cenario==2:
        guardas.draw()
        cultista.draw()
    if cenario==3:
        caebralum.draw()

def moveEnemy(janela,player,enemy,movimento,chao,checkPosInimigo):
    if (enemy.x<player.x and enemy.x>-5):
        enemy.x += movimento * janela.delta_time()
        checkPosInimigo=0
    elif (enemy.x>player.x and enemy.x<janela.width+5):
        enemy.x -= movimento * janela.delta_time()
        checkPosInimigo=1
    if (enemy.y>player.y and enemy.y-enemy.height>chao.height):
        enemy.y-= (movimento*3/4) * janela.delta_time()
    elif (enemy.y<player.y and enemy.y<janela.height-enemy.height):
        enemy.y+= (movimento*3/4) * janela.delta_time()
    return checkPosInimigo

def criaProjetilInimigo(cultista,listaProjeteisInimigoE,listaProjeteisInimigoD, checkTiroInimigo):
    # Crio o projetil
    if (checkTiroInimigo==1):
        projetilEsq = Sprite("MagiaCultista.png",1)
        projetilEsq.x = cultista.x
        projetilEsq.y = cultista.y+cultista.height/4
        listaProjeteisInimigoE.append(projetilEsq)

    elif (checkTiroInimigo==0):
        projetilDir = Sprite("MagiaCultista_invertido.png",1)
        projetilDir.x = cultista.x
        projetilDir.y = cultista.y+cultista.height/4
        listaProjeteisInimigoD.append(projetilDir)

def magicAttackInimigo(janela, listaProjeteisInimigoE, listaProjeteisInimigoD, velProjetil):
    for i in listaProjeteisInimigoD:
        i.x += velProjetil*janela.delta_time()
        i.draw()
        if (i.x>janela.width or i.x<0):
            listaProjeteisInimigoD.remove(i)
    for j in listaProjeteisInimigoE:
        j.x += (velProjetil*janela.delta_time())*-1
        j.draw()
        if (j.x>janela.width or j.x<0):
            listaProjeteisInimigoE.remove(j)
