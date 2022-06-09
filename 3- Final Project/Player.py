from PPlay.window import*
from PPlay.animation import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.collision import*
from PPlay.keyboard import*

def criaPlayer(janela,player,checkTiro):
    if checkTiro==0:
        playerD = Sprite("Emih.png", 1)
        playerD.x = player.x
        playerD.y = player.y
        return playerD
    elif checkTiro==1:
        playerE = Sprite("Emih_invertido.png", 1)
        playerE.x = player.x
        playerE.y = player.y
        return playerE
def movePlayer(janela,teclado,player,movimento,chao,checkTiro):
    if ((teclado.key_pressed("A") or teclado.key_pressed("LEFT")) and player.x>0):
        player.x -= movimento * janela.delta_time()
        checkTiro=1
    if ((teclado.key_pressed("D") or teclado.key_pressed("RIGHT")) and player.x<janela.width-player.width):
        player.x += movimento * janela.delta_time()
        checkTiro=0
    if ((teclado.key_pressed("W") or teclado.key_pressed("UP")) and player.y-player.height>chao.height):
        player.y-= (movimento/2) * janela.delta_time()
    if ((teclado.key_pressed("S") or teclado.key_pressed("DOWN")) and player.y<janela.height-player.height):
        player.y+= (movimento/2) * janela.delta_time()
    return checkTiro

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

def magicAttack(janela, listaProjeteisE, listaProjeteisD, velProjetil, checkTiro):
        if (checkTiro==0):
            for i in listaProjeteisD:
                i.x += velProjetil*janela.delta_time()
                i.draw()
                if (i.x>janela.width or i.x<0):
                    listaProjeteisD.remove(i)
        if (checkTiro==1):
            for j in listaProjeteisE:
                j.x += (velProjetil*janela.delta_time())*-1
                j.draw()
                if (j.x>janela.width or j.x<0):
                    listaProjeteisE.remove(j)
