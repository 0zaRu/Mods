import json
import os
import uuid
import pygame

'''====================================================================================   SEPARADO  ===================================================================================================================='''

def get_minecraft_launcher_profiles_path():
    appdata_roaming = os.getenv('APPDATA')
    if appdata_roaming:
        return os.path.join(appdata_roaming, '.minecraft', 'launcher_profiles.json')
    else:
        raise EnvironmentError("APPDATA environment variable not found.")

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def generate_unique_id(existing_ids):
    new_id = uuid.uuid4().hex
    while new_id in existing_ids:
        new_id = uuid.uuid4().hex
    return new_id

def add_profile(target_path, source_path, profile_id):

    target_data = load_json(target_path)
    source_data = load_json(source_path)
    
    if profile_id in source_data["profiles"]:
        new_profile = source_data["profiles"][profile_id]
        existing_ids = set(target_data["profiles"].keys())
        
        if profile_id in existing_ids:

            new_id = generate_unique_id(existing_ids)
            target_data["profiles"][new_id] = new_profile
        else:
            target_data["profiles"][profile_id] = new_profile
    else:
        printNot(f"Profile ID {profile_id} not found in source JSON.")
    
    save_json(target_path, target_data)


def install_separately():
    try:
        JSON_SOURCE = '.minecraft_data/source.json'
        JSON_TARGET = get_minecraft_launcher_profiles_path()
        # JSON_TARGET = './target.json'

        # Asegurarse de que las rutas a los archivos existan
        if os.path.exists(JSON_TARGET) and os.path.exists(JSON_SOURCE):
            add_profile(JSON_TARGET, JSON_SOURCE, "51a13bc528a4366b17e657cb22890a64")
            printNot("Perfil instalado por separado del .minecraft.")
        else:
            printNot("Una o ambas rutas de los archivos JSON no existen.", (220, 20, 20))
            
    except EnvironmentError as e:
        printNot(e, (220, 20, 20))
        

'''=====================================================================================   EN .MINECRAF   ==================================================================================================================='''
        
def install_in():
    try:
        JSON_SOURCE = './source.json'
        JSON_TARGET = get_minecraft_launcher_profiles_path()

        # Asegurarse de que las rutas a los archivos existan
        if os.path.exists(JSON_TARGET) and os.path.exists(JSON_SOURCE):
            add_profile(JSON_TARGET, JSON_SOURCE, "51a13bc528a4366b17e657cb22890a64")
            printNot("Perfil instalado por separado del .minecraft.")
        else:
            printNot("Una o ambas rutas de los archivos JSON no existen.", (220, 20, 20))
            
    except EnvironmentError as e:
        printNot(e, (220, 20, 20))


'''========================================================================================================================================================================================================'''


def main():
    pygame.init()

    width, height = 500, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Instalador de Perfiles de Minecraft")
    font = pygame.font.Font(None, 26)
    
    white = (255, 255, 255)
    black = (30, 30, 30)
    purple1 = (118, 0, 188)
    purple2 = (202, 92, 221)

    button_rect = pygame.Rect(30, 50, 440, 50)
    text = font.render("Instalar por separado del .minecraft (recomendado)", True, white)
    text_rect = text.get_rect(center=button_rect.center)

    button_rect2 = pygame.Rect(30, 120, 440, 50)
    text2 = font.render("Instalar en .minecraft", True, white)
    text_rect2 = text2.get_rect(center=button_rect2.center)
    
    button_rect3 = pygame.Rect(30, 240, 440, 100)
    
    text_lines = [
        "En caso de que elijas por separado, se creará ",
        "una carpeta \"Server Minecraft 2024\" ",
        "en la ruta especificada o por defecto, porque",
        " el juego se lanza desde ahí. En caso de instalar ",
        "sobre .minecraft se reemplazarán algunas ",
        "configuraciones y se borrará el contenido",
        "previo de la carpeta de mods.",
        "",
        "Si todo va bien, al abrir el juego estará",
        "la intalación \"Server Minecraft 2024\" para jugar."
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


    running = True
    while running:
        screen.fill((30, 30, 30))
        
        pygame.draw.rect(screen, purple1, button_rect)
        pygame.draw.rect(screen, purple2, button_rect2)
        pygame.draw.rect(screen, purple1, change_path_button_rect)
        screen.blit(text, text_rect)
        screen.blit(text2, text_rect2)
        screen.blit(text_surface, text_rect3)
        screen.blit(change_path_text, change_path_text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    install_separately()
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
