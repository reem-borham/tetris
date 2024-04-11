import pygame
import time

def play_music(mp3file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()
