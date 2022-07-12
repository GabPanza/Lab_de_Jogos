import pygame

def recarga(movimentoInimigo,delay):
    if (movimentoInimigo==100 or movimentoInimigo==-100):
        delay = 180
    if (movimentoInimigo==120 or movimentoInimigo==-120):
        delay = 150
    if (movimentoInimigo==150 or movimentoInimigo==-150):
        delay = 120
    return delay
def recargaCultistaInimigo(movimentoInimigo,delayInimigo):
    if (movimentoInimigo==100 or movimentoInimigo==-100):
        delayInimigo = 150
    if (movimentoInimigo==120 or movimentoInimigo==-120):
        delayInimigo = 125
    if (movimentoInimigo==150 or movimentoInimigo==-150):
        delayInimigo = 100
    return delayInimigo
