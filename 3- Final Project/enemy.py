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

def moveEnemy(janela,player,enemy,movimento,chao,checkPosInimigo):
    if (enemy.x<player.x and enemy.x>-5):
        enemy.x += (movimento/2) * janela.delta_time()
        checkPosInimigo=0
    elif (enemy.x>player.x and enemy.x<janela.width+5):
        enemy.x -= (movimento/2) * janela.delta_time()
        checkPosInimigo=1
    if (enemy.y>player.y - player.height/2):
        enemy.y-= (movimento/5) * janela.delta_time()
    elif (enemy.y<player.y - player.height/2):
        enemy.y+= (movimento/5) * janela.delta_time()
    return checkPosInimigo

def moveEnemyRanged(janela,player,enemy,movimento):
    if (enemy.y>player.y - player.height/2):
        enemy.y-= (movimento/5) * janela.delta_time()
    elif (enemy.y<player.y - player.height/2):
        enemy.y+= (movimento/5) * janela.delta_time()

def criaProjetilInimigo(cultista,listaProjeteisInimigo):
    projetil = Sprite("MagiaCultista.png",1)
    projetil.x = cultista.x
    projetil.y = cultista.y+cultista.height/3
    listaProjeteisInimigo.append(projetil)

def magicAttackInimigo(janela, player, vidasPlayer, listaProjeteisInimigo, velProjetil, delayInv):
    for i,projetil in enumerate(listaProjeteisInimigo):
        projetil.x -= velProjetil*janela.delta_time()
        projetil.draw()
        if (projetil.x<0):
            listaProjeteisInimigo.pop(i)

def enemy_melee_attack(enemy,player,vidasPlayer,delayInv):
    if enemy.collided(player):
        vidasPlayer-=1
        delayInv= 120
    return vidasPlayer, delayInv

def enemy_ranged_attack(listaProjeteisInimigo,player,vidasPlayer,delayInv):
    for i,projetil in enumerate(listaProjeteisInimigo):
        if projetil.collided(player):
            vidasPlayer-=1
            delayInv= 120
            listaProjeteisInimigo.pop(i)
    return vidasPlayer, delayInv

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

def hitCasteloCultista(listaProjeteisE,listaProjeteisD,cultista,vidasCultista):
    for i,projetil in enumerate(listaProjeteisE):
        if projetil.collided(cultista):
            vidasCultista-=1
            listaProjeteisE.pop(i)
    for i,projetil in enumerate(listaProjeteisD):
        if projetil.collided(cultista):
            vidasCultista-=1
            listaProjeteisD.pop(i)
    return vidasCultista

def hitCasteloGuardas(listaProjeteisE,listaProjeteisD,guardas,vidasGuardas):
    for i,projetil in enumerate(listaProjeteisE):
        if projetil.collided(guardas):
            vidasGuardas-=1
            listaProjeteisE.pop(i)
    for i,projetil in enumerate(listaProjeteisD):
        if projetil.collided(guardas):
            vidasGuardas-=1
            listaProjeteisD.pop(i)
    return vidasGuardas

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