import json

def cargar_datos(file_path, data):
    print("Cargando datos...")
    with open(file_path) as f_obj:
        data = json.load(f_obj)

def guardar_datos(file_path, data):
    with open(file_path, 'w') as f_obj:
        json.dump(data, f_obj)



