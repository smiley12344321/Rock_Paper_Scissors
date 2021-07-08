import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

pygame.mouse.set_cursor(pygame.cursors.diamond)
mouseX, mouseY = pygame.mouse.get_pos()
print(mouseX)
print(mouseY)

FPS = 30
FramePerSec = pygame.time.Clock()

RED = pygame.Color(255, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)

MYDISPLAY = pygame.display.set_mode((900, 600))
MYDISPLAY.fill(WHITE)
pygame.display.set_caption("Rock Paper Scissors")

pygame.draw.rect(MYDISPLAY, GREEN, (100, 400, 300, 150), 0)
pygame.draw.rect(MYDISPLAY, GREEN, (500, 400, 300, 150), 0)

Font1 = pygame.font.SysFont('jokerman', 72, bold=False, italic=False)
img1 = pygame.font.Font.render(Font1, str("Rock Paper Scissors"), True, RED)
MYDISPLAY.blit(img1, (100,100))
img2 = pygame.font.Font.render(Font1, str("Start"), True, RED)
MYDISPLAY.blit(img2, (160,425))
img3 = pygame.font.Font.render(Font1, str("Info"), True, RED)
MYDISPLAY.blit(img3, (580,425))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        pygame.event.get()
        (left, right, middle) = pygame.mouse.get_pressed(num_buttons=3)
        mouseX, mouseY = pygame.mouse.get_pos()
        if 100 < mouseX < 400 and 400 < mouseY < 550 and left == True:
            print("Yay")
        if 500 < mouseX < 800 and 400 < mouseY < 550 and left == True:
            print("Let's gooo")
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        FramePerSec.tick(FPS)
