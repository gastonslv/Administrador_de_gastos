""""
Gestor de gastos
"""
from funciones.f_menu import menu_principal as menu
from funciones.f_calcular import calcular

## caja 1
fondos = [0]

## caja 2
ahorros = [0]

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
    if usuario < 5:
        calcular(usuario, fondos, ahorros, gastos, ingresos, movimientos)
    else:
        salir_programa = True

