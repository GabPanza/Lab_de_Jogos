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
        enemy.x += (movimento*3/5) * janela.delta_time()
        checkPosInimigo=0
    elif (enemy.x>player.x and enemy.x<janela.width+5):
        enemy.x -= (movimento*3/5) * janela.delta_time()
        checkPosInimigo=1
    if (enemy.y>player.y and enemy.y-enemy.height>chao.height):
        enemy.y-= (movimento*2/5) * janela.delta_time()
    elif (enemy.y<player.y and enemy.y<janela.height-enemy.height):
        enemy.y+= (movimento*2/5) * janela.delta_time()
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
def hitFloresta(listaProjeteisE,listaProjeteisD,minotauro,vidasMinotauro):
    for i,projetil in enumerate(listaProjeteisE):
        if projetil.collided(minotauro):
            vidasMinotauro-=1
            listaProjeteisE.pop(i)
    for i,projetil in enumerate(listaProjeteisD):
        if projetil.collided(minotauro):
            vidasMinotauro-=1
            listaProjeteisD.pop(i)
    return vidasMinotauro

def hitCastelo(listaProjeteisE,listaProjeteisD,guardas,vidasGuardas,cultista,vidasCultista):
    for i,projetil in enumerate(listaProjeteisE):
        if projetil.collided(cultista):
            vidasCultista-=1
            listaProjeteisE.pop(i)
        if projetil.collided(guardas):
            vidasGuardas-=1
            listaProjeteisE.pop(i)
    for i,projetil in enumerate(listaProjeteisD):
        if projetil.collided(cultista):
            vidasCultista-=1
            listaProjeteisD.pop(i)
        if projetil.collided(guardas):
            vidasGuardas-=1
            listaProjeteisD.pop(i)
    return vidasCultista,vidasGuardas

def hitDungeon(listaProjeteisE,listaProjeteisD,caebralum,vidasCaebralum):
    for i,projetil in enumerate(listaProjeteisE):
        if projetil.collided(caebralum):
            vidasCaebralum-=1
            listaProjeteisE.pop(i)
    for i,projetil in enumerate(listaProjeteisD):
        if projetil.collided(caebralum):
            vidasCaebralum-=1
            listaProjeteisD.pop(i)
    return vidasCaebralum