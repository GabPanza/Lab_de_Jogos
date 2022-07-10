from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*

def SetPlayer(PlayerState,playerAtual):
    player = PlayerState
    player.x = playerAtual.x
    player.y = playerAtual.y
    return player

def movePlayer(janela,teclado,player,movimento,chao,checkPos):
    if ((teclado.key_pressed("A") or teclado.key_pressed("LEFT")) and player.x>-5):
        player.x -= movimento * janela.delta_time()
        checkPos=1
    elif ((teclado.key_pressed("D") or teclado.key_pressed("RIGHT")) and player.x<janela.width-player.width/2):
        player.x += movimento * janela.delta_time()
        checkPos=0
    if ((teclado.key_pressed("W") or teclado.key_pressed("UP")) and player.y+player.height>=chao.y):
        player.y-= (movimento*3/4) * janela.delta_time()
    elif ((teclado.key_pressed("S") or teclado.key_pressed("DOWN")) and player.y+player.height<janela.height):
        player.y+= (movimento*3/4) * janela.delta_time()
    return checkPos

def criaProjetil(player,listaProjeteisE,listaProjeteisD, checkTiro):
    # Crio o projetil
    if (checkTiro==1):
        projetilEsq = Sprite("MagiaEmih.png",1)
        projetilEsq.x = player.x
        projetilEsq.y = player.y+player.height/4
        listaProjeteisE.append(projetilEsq)

    elif (checkTiro==0):
        projetilDir = Sprite("MagiaEmih_invertido.png",1)
        projetilDir.x = player.x
        projetilDir.y = player.y+player.height/4
        listaProjeteisD.append(projetilDir)

def magicAttack(janela, listaProjeteisE, listaProjeteisD, velProjetil):
    for i in listaProjeteisD:
        i.x += velProjetil*janela.delta_time()
        i.draw()
        if (i.x>janela.width or i.x<0):
            listaProjeteisD.remove(i)
    for j in listaProjeteisE:
        j.x -= (velProjetil*janela.delta_time())
        j.draw()
        if (j.x>janela.width or j.x<0):
            listaProjeteisE.remove(j)