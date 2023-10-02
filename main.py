""""
Gestor de gastos
"""

from funciones.f_menu import menu_principal as menu

# Variables
salir_programa = False
d_usuario_menu = 0 # futura decision del usuario

print("Bienvenido al gestor de gastos!")

while salir_programa == False:
    d_usuario_menu = menu()
    print(d_usuario_menu)

