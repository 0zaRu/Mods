import misPygame as mp
import shutil
import launch_create as lc
import os

def instalacionExterna(RUTA):
    # descargar y descomprimir
    # mp.descargarRepo(RUTA_TEMP, lambda p: p)
    
    # comprobar ruta con ruta_temp y si son iguales no hacer nada
    if os.path.exists(RUTA+"minecraft_data"):
        shutil.rmtree(RUTA+"minecraft_data")
    
    try:
        shutil.copytree("./minecraft_data", RUTA+"/servidor_2024", dirs_exist_ok=True)
    except OSError as e:
        # mp.printNot(f"{e}")
        print(f"{e}")
    
    # llamar al creador de perfil de launcher diciendo la ruta donde está el juego
    lc.create_external(RUTA+"\servidor_2024")
    
def instalacionEnMinecraft(RUTA):
    mp.printNot("A Alberto le dió pereza, copia de minecraft_data y pega en .minecraft")