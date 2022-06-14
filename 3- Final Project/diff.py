from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.gameimage import *

def diff():
    janela = Window(1280,720)

    teclado = janela.get_keyboard()

    mouseClick = janela.get_mouse()

    facil = Sprite("facil.png", 1)
    medio = Sprite("medio.png", 1)
    dificil = Sprite("dificil.png", 1)
    
    # Instancio o fundo
    fundo = GameImage("FundoInicial.jpg")
    
    while (True):
        # Desenho  o fundo
        fundo.draw()
        
        if(teclado.key_pressed("ESC")):
            import menu
            menu.menu()
        
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(facil)):
            from main import game
            game(vidas=5,vidasInimigo=3,movimento=200,movimentoInimigo=100,velProjetil=900,velProjetilInimigo=450,delay=0,delayInimigo=100)
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(medio)):
            from main import game
            game(vidas=4,vidasInimigo=4,movimento=200,movimentoInimigo=100,velProjetil=900,velProjetilInimigo=450,delay=0,delayInimigo=100)
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(dificil)):
            from main import game
            game(vidas=3,vidasInimigo=5,movimento=200,movimentoInimigo=100,velProjetil=900,velProjetilInimigo=450,delay=0,delayInimigo=100)
        
        facil.set_position(492, 300)
        medio.set_position(490, 400)
        dificil.set_position(508, 500)
        
        janela.draw_text(("DIFICULDADES"), (janela.width / 2)-220, 50, size=48, font_name="Arial", bold=True,color=[200, 0, 255])
        facil.draw()
        medio.draw()
        dificil.draw()
        
        janela.set_title("Space Invaders")

        janela.update()
diff()