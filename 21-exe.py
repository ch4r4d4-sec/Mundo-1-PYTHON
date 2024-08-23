#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÀUDIO DE UM ARQUIVO MP3.

#Forma um.
'''import webbrowser
webbrowser.open('21-exe.mp3')'''


#Forma dois.
import pygame

pygame.init()
pygame.mixer.music.load('21-exe.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()