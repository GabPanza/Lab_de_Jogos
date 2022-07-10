from PPlay.window import*
from PPlay.keyboard import*
from PPlay.sound import*
import pygame
from pygame import mixer

def vitoria():
    # Instancio o tamanho da janela
    janela = Window(1280,720)
    
    # Inicializo o teclado
    teclado = janela.get_keyboard()
    
    # Adiciono musica
    mixer.music.load("VictoryThemeSoundtrack.wav")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    
    while True:
        # Desenho o fundo
        
        
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            mixer.music.stop()
            import menu
            menu.menu()
        # Desenho os textos finais
        janela.draw_text(("Parabéns, nova Rainha. O reino está salvo desta criatura graças a você!"), (janela.width/2)-480, janela.height/2, size=28, font_name="Arial", bold=True,color=[255, 255, 0])

        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()

def derrota():
    # Instancio o tamanho da janela
    janela = Window(1280,720)
    
    # Inicializo o teclado
    teclado = janela.get_keyboard()
    
    # Adiciono musica
    mixer.music.load("DefeatThemeSoundtrack.wav")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    
    while True:
        # Desenho o fundo
        
        
        # Volto pro menu
        if (teclado.key_pressed("ESC")):
            mixer.music.stop()
            import menu
            menu.menu()
        
        # Desenho os textos finais
        janela.draw_text(("Eh... parece que você nao estava pronto mesmo. O reino sentirá sua falta, princesa!"), (janela.width/2)-555, janela.height/2, size=28, font_name="Arial", bold=True,color=[255, 255, 0])
        
        # Define um titulo pra janela
        janela.set_title("A Ascensão da Feiticeira")
        
        # Finaliza o Gameloop
        janela.update()