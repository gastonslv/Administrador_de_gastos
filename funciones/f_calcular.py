from f_calcular_gastos import calcular_gastos as  c_gastos

def calcular(operacion, fondos, ahorros, gastos, ingresos, movimientos):
    if operacion == 1:
        c_gastos(fondos, gastos, movimientos)
    return 0


