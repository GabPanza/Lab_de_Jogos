from PPlay.window import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.sound import *

def instrucao():
    # Instancio a janela
    janela = Window(1280,720)

    # Inicializo o teclado
    teclado = janela.get_keyboard()

    # Instancio o mouse
    mouseClick = janela.get_mouse()
    
    # Instancio as imagens dos botões
    playButton=Sprite("Play.png",1)
    playButton.set_position(janela.width/2 - playButton.width/2, janela.height - 200)

    while True:
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            from menu import menu
            menu()
            
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(playButton)):
            from main import game
            game(vidas=5,vidasInimigo=3,movimento=200,movimentoInimigo=100,velProjetil=900,velProjetilInimigo=300,delay=0,delayInimigo=100)
        
        # Desenho o fundo
        janela.set_background_color([0,0,0])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Desenho as instrucoes
        janela.draw_text(("Instruçoes"), (janela.width / 2)-100, 100, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        janela.draw_text(("Se aproxime de uma placa sempre que se sentir perdido. Elas te guiarão."), 100, 150, size=32, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Pressione 'W,A,S,D' ou as setas do teclado para andar."), 100, 200, size=32, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Pressione 'Space' para atirar."), 100, 250, size=32, font_name="Arial", bold=True,color=[255, 255, 255])

        # Desenho o botao
        playButton.draw()
        
        # Atualizo o gameLoop
        janela.update()
