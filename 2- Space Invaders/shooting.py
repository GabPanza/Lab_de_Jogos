from PPlay.sprite import*
from PPlay.collision import*
import pygame
import random

def criaProjNave(player,listaProjeteis):
    # Crio o projetil
    projetil = Sprite("projetil.png",1)
    projetil.x = player.x + 50
    projetil.y = player.y - projetil.height
    listaProjeteis.append(projetil)

def tiroPlayer(janela,listaProjeteis,velProjetil):
    for i in listaProjeteis:
        i.y -= velProjetil*janela.delta_time()
        i.draw()
        if (i.y<-50):
            listaProjeteis.remove(i)

def criaProjInimigo(inimigo,listaProjeteisInimigos):
    # Crio o projetil
    projetilInimigo = Sprite("projetil2.png",1)
    projetilInimigo.x = inimigo.x + 50
    projetilInimigo.y = inimigo.y + projetilInimigo.height + 50
    if (random.random() < 0.11):
        listaProjeteisInimigos.append(projetilInimigo)

def tiroInimigo(janela,listaProjeteisInimigos,velProjetilInimigo):
    for i,projetilAlien in enumerate(listaProjeteisInimigos):
        projetilAlien.y += velProjetilInimigo*janela.delta_time()
        projetilAlien.draw()
        if (projetilAlien.y>janela.height):
            listaProjeteisInimigos.pop(i)

def criaProjNaveMae(navemae,listaProjeteisNavemae):
    # Crio o projetil
    projetilInimigo = Sprite("projetil2.png",1)
    projetilInimigo.x = navemae.x + 20
    projetilInimigo.y = navemae.y + projetilInimigo.height + 50
    if (random.random() < 0.3):
        listaProjeteisNavemae.append(projetilInimigo)
    
def tiroNaveMae(janela,listaProjeteisNavemae,velProjetilInimigo):
    for i,projetilNavemae in enumerate(listaProjeteisNavemae):
        projetilNavemae.y += velProjetilInimigo*janela.delta_time()
        projetilNavemae.draw()
        if (projetilNavemae.y>janela.height):
            listaProjeteisNavemae.pop(i)

def delay(movimentoInimigo,delay):
    if (movimentoInimigo==100 or movimentoInimigo==-100):
        delay = 55
    if (movimentoInimigo==120 or movimentoInimigo==-120):
        delay = 45
    if (movimentoInimigo==150 or movimentoInimigo==-150):
        delay = 35
    return delay
def delayInimigo(movimentoInimigo,delayInimigo):
    if (movimentoInimigo==100 or movimentoInimigo==-100):
        delayInimigo = 100
    if (movimentoInimigo==120 or movimentoInimigo==-120):
        delayInimigo = 125
    if (movimentoInimigo==150 or movimentoInimigo==-150):
        delayInimigo = 150
    return delayInimigo
