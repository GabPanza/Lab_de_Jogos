from PPlay.window import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.sound import *
import main

def instrucaoBoss(movimentoInimigo,vidas):
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
                main.game(vidas=vidas,vidasInimigo=3,movimento=200,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100,cenario=3)
            elif(movimentoInimigo==120):
                main.game(vidas=vidas,vidasInimigo=3,movimento=200,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100,cenario=3)
            elif(movimentoInimigo==150):
                main.game(vidas=vidas,vidasInimigo=5,movimento=200,movimentoInimigo=movimentoInimigo,velProjetil=600,velProjetilInimigo=300,delay=0,delayInimigo=100,cenario=3)
        # Desenho o fundo
        janela.set_background_color([0,0,0])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Desenho as instrucoes
        janela.draw_text(("Instruçoes"), (janela.width / 2)-128, 100, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        janela.draw_text(("Esta luta usará tudo o que voce aprendeu ate agora."), 200, 150, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Quando se sentir pronto, clique em Jogar."), 200, 200, size=28, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Controles"), (janela.width / 2)-128, 250, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        janela.draw_text(("Pressione 'W,A,S,D' ou as setas do teclado para andar."), 200, 300, size=32, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Pressione 'Space' para atirar."), 400, 350, size=32, font_name="Arial", bold=True,color=[255, 255, 255])

        # Desenho o botao
        playButton.draw()
        
        # Atualizo o gameLoop
        janela.update()
