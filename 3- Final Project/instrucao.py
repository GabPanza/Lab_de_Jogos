from PPlay.window import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.sound import *
import main

def instrucao(movimentoInimigo):
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
            import menu
            menu.menu()
            
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(playButton)):
            if(movimentoInimigo==100):
                main.game(vidas=5,vidasInimigo=4,movimento=200,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100,cenario=1,summon=False)
            elif(movimentoInimigo==120):
                main.game(vidas=5,vidasInimigo=4,movimento=200,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100,cenario=1,summon=False)
            elif(movimentoInimigo==150):
                main.game(vidas=3,vidasInimigo=5,movimento=200,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100,cenario=1,summon=False)
        # Desenho o fundo
        janela.set_background_color([0,0,0])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Desenho as instrucoes
        janela.draw_text(("Instruçoes"), (janela.width / 2)-128, 100, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        janela.draw_text(("Alguns eventos no jogo dependem que certas condiçoes aconteçam."), 200, 150, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Logo, sempre que estiver perdido, se aproxime de uma placa."), 200, 200, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Ela te guiará para onde deve ir"), 200, 250, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Controles"), (janela.width / 2)-128, 300, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        janela.draw_text(("Pressione 'W,A,S,D' ou as setas do teclado para andar."), 200, 350, size=32, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Pressione 'Space' para atirar."), 400, 400, size=32, font_name="Arial", bold=True,color=[255, 255, 255])

        # Desenho o botao
        playButton.draw()
        
        # Atualizo o gameLoop
        janela.update()
