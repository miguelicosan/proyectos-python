import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e Icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("icons\\icono.png")
pygame.display.set_icon(icono)

# Loop del juego
en_ejecucion = True
while en_ejecucion:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            
            en_ejecucion = False

    # Color fondo pantalla
    pantalla.fill((205, 144, 228))
    pygame.display.update()