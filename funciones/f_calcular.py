from funciones.f_operaciones import calcular_gastos as  c_gastos
from funciones.f_operaciones import calcular_ingresos as  c_ingresos

def calcular(operacion, fondos, ahorros, gastos, ingresos, movimientos):
    if operacion == 1:
        c_gastos(fondos, gastos, movimientos)
    elif operacion == 2:
        c_ingresos(fondos, ingresos, movimientos)
    return 0


