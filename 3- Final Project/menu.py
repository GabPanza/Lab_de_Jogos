from PPlay.window import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.sound import *

def menu():    
    # Instancio a janela
    janela = Window(1280,720)

    # Instancio o mouse
    mouseClick = janela.get_mouse()
    
    # Instancio as imagens dos botões
    playButton=Sprite("Play.png",1)
    diffButton=Sprite("Dificuldade.png",1)
    leaveButton=Sprite("Sair.png",1)

    while (True):
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(playButton)):
            from instrucao import instrucao
            instrucao()
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(diffButton)):
            from diff import diff
            diff()
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(leaveButton)):
            from sair import sair
            sair()
        
        playButton.set_position(525, 260)
        diffButton.set_position(525, 335)
        leaveButton.set_position(525, 410)
        
        janela.set_background_color([0,0,0])

        playButton.draw()
        diffButton.draw()
        leaveButton.draw()
        
        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        janela.draw_text(("A Ascensão da Feiticeira"), (janela.width / 2)-285, 150, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        
        # Atualizo o Gameloop
        janela.update()
menu()