# Faça um programa em Python que abra e reproduza
# o áudio de um arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.05)
input()











