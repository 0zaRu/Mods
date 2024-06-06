import json
import os
import uuid
import misPygame as mp

'''====================================================================================   SEPARADO  ===================================================================================================================='''

def get_minecraft_launcher_profiles_path():
    appdata_roaming = os.getenv('APPDATA')
    if appdata_roaming:
        return os.path.join(appdata_roaming, '.minecraft', 'launcher_profiles.json')
    else:
        mp.printNot("APPDATA environment variable not found.")
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

def add_profile(target_path, source_path, profile_id, RUTA):
    target_data = load_json(target_path)
    source_data = load_json(source_path)
    
    RUTA.replace("\\", "\\\\")

    if profile_id in source_data["profiles"]:
        new_profile = source_data["profiles"][profile_id]
        existing_ids = set(target_data["profiles"].keys())

        if profile_id in existing_ids:
            new_id = generate_unique_id(existing_ids)
            target_data["profiles"][new_id] = new_profile
        else:
            target_data["profiles"][profile_id] = new_profile

        # Cambiar la ruta guardada en el perfil con la etiqueta "gameDir" a la variable RUTA
        if "gameDir" in new_profile:
            new_profile["gameDir"] = RUTA
        else:
            new_profile["gameDir"] = RUTA  # Si "gameDir" no existe en el perfil, lo agregamos

    else:
        mp.printNot(f"Profile ID {profile_id} not found in source JSON.")

    save_json(target_path, target_data)


def create_external(RUTA):
    try:
        JSON_SOURCE = './minecraft_data/source.json'
        JSON_TARGET = get_minecraft_launcher_profiles_path()

        # Asegurarse de que las rutas a los archivos existan
        if os.path.exists(JSON_TARGET):
            if os.path.exists(JSON_SOURCE):
                add_profile(JSON_TARGET, JSON_SOURCE, "51a13bc528a4366b17e657cb22890a64", RUTA)
                mp.printNot("Perfil instalado por separado del .minecraft.")
                return True
            else:
                mp.printNot("Perfil a instalar no encontrado, creelo manualmente en minecraft launcher", (220, 20, 20))
        else:
            mp.printNot("Probablemente no tengas minecraft comprado, instala los mods en .minecraft", (220, 20, 20))
        
            
    except EnvironmentError as e:
        mp.printNot(e, (220, 20, 20))
    
    return False
        

'''=====================================================================================   EN .MINECRAF   ==================================================================================================================='''
        
def create_in():
    try:
        JSON_SOURCE = './source.json'
        JSON_TARGET = get_minecraft_launcher_profiles_path()

        # Asegurarse de que las rutas a los archivos existan
        if os.path.exists(JSON_TARGET) and os.path.exists(JSON_SOURCE):
            add_profile(JSON_TARGET, JSON_SOURCE, "51a13bc528a4366b17e657cb22890a64")
            mp.printNot("Perfil instalado por separado del .minecraft.")
        else:
            mp.printNot("Una o ambas rutas de los archivos JSON no existen.", (220, 20, 20))
            
    except EnvironmentError as e:
        mp.printNot(e, (220, 20, 20))


'''========================================================================================================================================================================================================'''
