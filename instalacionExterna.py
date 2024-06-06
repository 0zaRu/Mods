import misPygame as mp
import shutil
import launch_create as lc
import os

def instalacionExterna(RUTA):
    # llamar al creador de perfil de launcher diciendo la ruta donde está el juego
    if lc.create_external(RUTA+"\servidor_2024"):
        # comprobar ruta con ruta_temp y si son iguales no hacer nada
        if os.path.exists(RUTA+"minecraft_data"):
            shutil.rmtree(RUTA+"minecraft_data")
        
        try:
            shutil.copytree("./minecraft_data", RUTA+"/servidor_2024", dirs_exist_ok=True)
        except OSError as e:
            mp.printNot(f"{e}")
    
def instalacionEnMinecraft(RUTA):
    # llamar al creador de perfil de launcher diciendo la ruta donde está el juego
    if lc.create_external(RUTA+"\servidor_2024", pirata=True):
        # comprobar ruta con ruta_temp y si son iguales no hacer nada
        if os.path.exists(RUTA+"minecraft_data"):
            shutil.rmtree(RUTA+"minecraft_data")
        
        try:
            shutil.copytree("./minecraft_data", RUTA+"/servidor_2024", dirs_exist_ok=True)
        except OSError as e:
            mp.printNot(f"{e}")