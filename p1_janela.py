import pygame

pygame.init()

janela = pygame.display.set_mode((400,300))
pygame.display.set_caption("Olá mundo")

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

pygame.quit()