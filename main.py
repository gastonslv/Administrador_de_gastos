""""
Gestor de gastos
"""
import json
from funciones.f_menu import menu_principal as menu
from funciones.f_cargar_datos import * #json cargar_datos guardar_datos

## caja 1
fondos = []

## caja 2
ahorros = []

## registro de operaciones
gastos = []
ingresos = []
movimientos = []

## Variables
salir_programa = False
usuario = 0 # decision del usuario

print("Bienvenido al gestor de gastos!")

while salir_programa == False:
    usuario = menu(fondos, ahorros)
    
    if usuario >= 4:
        calcular(usuario, fondos, ahorros, gastos, ingresos, movimientos)
    else:
        salir_programa = True

