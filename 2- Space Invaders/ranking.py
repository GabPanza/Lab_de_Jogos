from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *

def rank():
    janela = Window(1280,720)

    teclado = janela.get_keyboard()

    espaco = GameImage("espaço.jpg")

    while (True):
        # Desenho o fundo
        espaco.draw()
        
        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            import menu
            menu.MainMenu()
        
        # Desenho as instruçoes da janela
        janela.draw_text(("RANKING"), (janela.width / 2)-150, 50, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Defino o titulo do jogo
        janela.set_title("Space Invaders")
        
        # Atualizo o GameLoop
        janela.update()

def fimDoJogoVitoria(score):
    janela = Window(1280,720)
    
    teclado = janela.get_keyboard()

    espaco = GameImage("espaço.jpg")
    
    
    
    while (True):
        # Desenho o fundo
        espaco.draw()
        
        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            import menu
            menu.MainMenu()
            
        janela.draw_text(("Você derrotou a invasão! Parabéns, recruta!"), (janela.width/2) - 350, janela.height/2 - 200, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Aperte 'ESC' para sair"), (janela.width/2) - 250, (janela.height/2) -100, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Instancio o titulo da janela  
        janela.set_title("Space Invaders")
        
        # Atualizo o GameLoop
        janela.update()

def fimDoJogoDerrota(score):
    janela = Window(1280,720)
    
    teclado = janela.get_keyboard()
    
    espaco = GameImage("espaço.jpg")
    
    
    
    while (True):
        # Desenho o fundo
        espaco.draw()

        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            import menu
            menu.MainMenu()
            
        janela.draw_text(("Você foi derrotado pela invasão! Boa sorte na proxima vez, recruta!"), (janela.width/2) - 400, janela.height/2 - 200, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Aperte 'ESC' para voltar ao menu"), (janela.width/2) - 250, (janela.height/2) - 100, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Instancio o titulo da janela  
        janela.set_title("Space Invaders")
        
        # Atualizo o GameLoop
        janela.update()