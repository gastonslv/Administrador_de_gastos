""""
Gestor de gastos
"""
import json
from funciones.f_menu import menu_principal as menu
from funciones.f_cargar_datos import * #json cargar_datos guardar_datos

## Variables
salir_programa = False
d_usuario_menu = 0 # futura decision del usuario

## Cargamos

gastos = []
ingresos = []
ahorros = []
fondos = []

print("Bienvenido al gestor de gastos!")

while salir_programa == False:
    d_usuario_menu = menu()
    

