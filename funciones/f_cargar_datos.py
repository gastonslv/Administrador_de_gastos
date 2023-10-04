import json

def cargar_datos(filename, data):
    print("Cargando datos...")
    with open(filename, 'w') as f_obj:
        data = json.load(f_obj)

def guardar_datos(filename, data):
    with open(filename, 'w') as f_obj:
        json.dump(data, f_obj)