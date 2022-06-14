import pygame

def recarga(movimentoInimigo,delay):
    if (movimentoInimigo==100 or movimentoInimigo==-100):
        delay = 100
    if (movimentoInimigo==120 or movimentoInimigo==-120):
        delay = 80
    if (movimentoInimigo==150 or movimentoInimigo==-150):
        delay = 60
    return delay
def recargaCultistaInimigo(movimentoInimigo,delayInimigo):
    if (movimentoInimigo==100 or movimentoInimigo==-100):
        delayInimigo = 100
    if (movimentoInimigo==120 or movimentoInimigo==-120):
        delayInimigo = 125
    if (movimentoInimigo==150 or movimentoInimigo==-150):
        delayInimigo = 150
    return delayInimigo
