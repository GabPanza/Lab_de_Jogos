from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *

def MainMenu():
    # Instancio a janela
    janela = Window(1280,720)

    # Instancio o mouse
    mouseClick = janela.get_mouse()
    
    # Instancio as imagens dos botões
    playButton=Sprite("Play.png")
    diffButton=Sprite("Dificuldade.png")
    rankingButton=Sprite("Ranking.png")
    leaveButton=Sprite("Sair.png")

    while (True):
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(playButton)):
            import main
            main.game(vidas=5,movimento=200,movimentoInimigo=100,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100,linha=3)
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(diffButton)):
            import diff
            diff.difficult()
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(rankingButton)):
            import ranking
            ranking.rank()
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(leaveButton)):
            import sair
            sair.sair()
        
        playButton.set_position(500, 200)
        diffButton.set_position(500, 275)
        rankingButton.set_position(500, 350)
        leaveButton.set_position(500, 425)
        
        janela.set_background_color([0,0,0])

        playButton.draw()
        diffButton.draw()
        rankingButton.draw()
        leaveButton.draw()
        
        janela.set_title("Space Invaders")

        janela.update()
MainMenu()