""""
Gestor de gastos
"""
from funciones.f_menu import menu_principal as menu
from funciones.f_calcular import calcular
from funciones.f_manipulacion_datos import cargar_datos, guardar_datos
## caja 1
fondos = cargar_datos("data\\fondos.json")

## caja 2
ahorros = cargar_datos("data\\ahorros.json")

## registro de operaciones
gastos = cargar_datos("data\\gastos.json")
ingresos = cargar_datos("data\\ingresos.json")
movimientos = cargar_datos("data\\movimientos.json")

## Variables
salir_programa = False
usuario = 0 # decision del usuario

print("Bienvenido al gestor de gastos!")

while salir_programa == False:
    usuario = menu(fondos, ahorros)
    if usuario < 5:
        calcular(usuario, fondos, ahorros, gastos, ingresos, movimientos)
    else:
        salir_programa = True

print("Guardando datos...")

guardar_datos("data\\fondos.json", fondos)
guardar_datos("data\\ahorros.json", ahorros)
guardar_datos("data\\gastos.json", gastos)
guardar_datos("data\\ingresos.json", ingresos)
guardar_datos("data\\movimientos.json", movimientos)