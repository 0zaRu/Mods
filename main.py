import pygame
import os
import instalacionExterna as ie
from tkinter import filedialog

width, height = 500, 500

white = (255, 255, 255)
black = (30, 30, 30)
purple1 = (118, 0, 188)
purple2 = (202, 92, 221)

def initPygame():
    pygame.init()
    
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Instalador de Perfiles de Minecraft")
    font = pygame.font.Font(None, 24)
    
    return screen, font

def initButtons(font, RUTA):
    button_rect = pygame.Rect(30, 50, 440, 50)
    text = font.render("Instalar por separado del .minecraft (recomendado)", True, white)
    text_rect = text.get_rect(center=button_rect.center)

    button_rect2 = pygame.Rect(30, 120, 440, 50)
    text2 = font.render("Instalar en .minecraft", True, white)
    text_rect2 = text2.get_rect(center=button_rect2.center)
    
    button_rect3 = pygame.Rect(30, 260, 440, 100)
    
    text_lines = [
        "En caso de que elijas por separado, se creará ",
        "una carpeta \"Server Minecraft 2024\" ",
        "en la ruta especificada o por defecto, porque",
        "el juego se lanza desde ahí. En caso de instalar ",
        "sobre .minecraft se reemplazarán algunas ",
        "configuraciones y se borrará el contenido",
        "previo de la carpeta de mods.",
        "La segunda no está hecha, solo copia todo lo de ",
        "minecraft_data y pégalo reemplazando en .minecraft",
        "(borra primero la carpeta mods de .minecraft)."
        "",
        "",
        "Si todo va bien, al abrir el juego estará la instalación ",
        "\"Server Minecraft 2024\" para darle a ",
        "directamente a jugar."
    ]
    line_height = font.get_linesize()
    text_surface = pygame.Surface((440, line_height * len(text_lines)))
    text_surface.fill(black)
    for i, line in enumerate(text_lines):
        rendered_line = font.render(line, True, white)
        text_surface.blit(rendered_line, (0, i * line_height))
    text_rect3 = text_surface.get_rect(center=button_rect3.center)


    # Botón para cambiar la ruta de instalación
    change_path_button_rect = pygame.Rect(width - 280, 10, 250, 30)
    change_path_text = font.render("Cambiar Ruta de Instalación", True, white)
    change_path_text_rect = change_path_text.get_rect(center=change_path_button_rect.center)
    
    # Botón para cambiar la ruta de instalación
    path_button_rect = pygame.Rect(30, 470, 250, 30)
    path_text = font.render(RUTA, True, (180, 180, 180))
    path_text_rect = path_text.get_rect(center=path_button_rect.center)
    
    return button_rect, text, text_rect, button_rect2, text2, text_rect2, button_rect3, text_surface, text_rect3, change_path_button_rect, change_path_text, change_path_text_rect, path_button_rect, path_text, path_text_rect

def main():
    RUTA = os.path.join(os.getenv('USERPROFILE'), 'Documents\Minecraft')
    RUTA_TEMP = os.path.join(os.getenv('USERPROFILE'), 'Documents\Minecraft')
    
    screen, font = initPygame()
    
    button_rect, text, text_rect, \
    button_rect2, text2, text_rect2, \
    button_rect3, text_surface, text_rect3, \
    change_path_button_rect, change_path_text, change_path_text_rect, \
    path_button_rect, path_text, path_text_rect \
        = initButtons(font, RUTA)

    
    running = True
    while running:
        screen.fill((30, 30, 30))
        
        pygame.draw.rect(screen, purple1, button_rect)
        pygame.draw.rect(screen, purple2, button_rect2)
        pygame.draw.rect(screen, purple1, change_path_button_rect)
        pygame.draw.rect(screen, black, path_button_rect)
        screen.blit(text, text_rect)
        screen.blit(text2, text_rect2)
        screen.blit(text_surface, text_rect3)
        screen.blit(change_path_text, change_path_text_rect)
        
        path_text = font.render(RUTA, True, (180, 180, 180))
        screen.blit(path_text, path_text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    ie.instalacionExterna(RUTA)
                    
                elif button_rect2.collidepoint(event.pos):
                    ie.instalacionEnMinecraft(RUTA)
                elif change_path_button_rect.collidepoint(event.pos):
                    RUTA = filedialog.askdirectory()
        
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
