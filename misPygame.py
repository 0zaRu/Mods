import pygame

def printNot(message, color_back=(30, 30, 30)):
    # Configurar colores
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    # Inicializar pygame y la pantalla
    pygame.init()
    screen = pygame.display.set_mode((800, 200))
    pygame.display.set_caption("Alerta")
    
    # Configurar la fuente predeterminada de pygame
    font = pygame.font.Font(None, 26)

    # Configurar el texto
    text = font.render(message, True, white)
    text_rect = text.get_rect(center=screen.get_rect().center)
    
    # Dibujar el fondo de la alerta
    alert_rect = pygame.Rect(0, 0, text_rect.width + 20, text_rect.height + 80)
    alert_rect.center = text_rect.center
    pygame.draw.rect(screen, color_back, alert_rect)
    
    # Dibujar el texto
    screen.blit(text, text_rect)
    
    # Definir la separación entre el texto y el botón
    separation = 30
    
    # Dibujar el botón OK
    button_rect = pygame.Rect(0, 0, 300, 40)
    button_rect.centerx = text_rect.centerx
    button_rect.top = text_rect.bottom + separation  # Separación de 30 píxeles
    pygame.draw.rect(screen, white, button_rect)
    button_text = font.render("Que si Alberto, déjame jugar", True, black)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Bucle para esperar el evento de cerrar la notificación
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False
    
    screen = pygame.display.set_mode((500, 500))
