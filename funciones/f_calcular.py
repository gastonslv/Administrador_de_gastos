from funciones.f_operaciones import calcular_gastos as  c_gastos
from funciones.f_operaciones import calcular_ingresos as  c_ingresos
from funciones.f_operaciones import calcular_ahorro as c_ahorro
from funciones.f_operaciones import mostrar_movimientos

def calcular(operacion, fondos, ahorros, gastos, ingresos, movimientos):
    if operacion == 1:
        c_gastos(fondos, gastos, movimientos)
    elif operacion == 2:
        c_ingresos(fondos, ingresos, movimientos)
    elif operacion == 3:
        c_ahorro(fondos, ahorros, movimientos)
    elif operacion == 4:
        mostrar_movimientos(movimientos)
    return 0


