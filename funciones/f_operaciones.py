def calcular_gastos(fondos, gastos, movimientos):
    """
    Le pide al usuario que ingrese su gasto. La funcion se encarga de descontar
    del fondo dicho gasto y registrar la operacion en gastos y movimientos
    """
    salir = False
    gasto = {}
    descripcion = '-'
    fecha = ''

    while salir == False:
        try:
            monto_gasto = float(input("Ingrese el monto del gasto: "))
            if monto_gasto > fondos[0]: # verificamos que hayan fondos
                print("No hay fondos suficientes para realizar la operacion.")
                salir = True # salimos de la operacion gastos, ya que no hay fondos
            else:
                print("Operacion exitosa!")
                fondos[0] -= monto_gasto # modificamos el fondo
                descripcion = input("Descripcion del gasto: ")
                fecha = input("Fecha [01/01/01]: ")
                gasto = {
                    'monto': monto_gasto,
                    'resumen': descripcion,
                    'fecha': fecha,
                    }
                gastos.append(gasto)
                gasto = {
                    'tipo': 'gasto',
                    'monto': monto_gasto,
                    'resumen': descripcion,
                    'fecha': fecha,
                    }
                movimientos.append(gasto)
                salir = True
        except ValueError:
            print("\n--------Error--------")
            print("El valor que ingreso es incorrecto, vuelava a intentarlo")
            print("---------------------\n")
            continue


def calcular_ingresos(fondos, ingresos, movimientos):
    salir = False
    ingreso = {}
    descripcion = '-'
    fecha = ''

    while salir == False:
        try:
            monto_ingreso = float(input("Ingrese el monto del ingreso: "))
            fondos[0] += monto_ingreso # agregamos los ingresos al fondo
            descripcion = input("Descripcion del ingreso: ")
            fecha = input("Fecha [01/01/01]: ")
            ingreso = {
                'monto': monto_ingreso,
                'resumen': descripcion,
                'fecha': fecha,
                }
            ingresos.append(ingreso)
            ingreso = {
                'tipo': 'ingreso',
                'monto': monto_ingreso,
                'resumen': descripcion,
                'fecha': fecha,
                }
            movimientos.append(ingreso)
            salir = True
        except ValueError:
            print("\n--------Error--------")
            print("El valor que ingreso es incorrecto, vuelava a intentarlo")
            print("---------------------\n")
            continue

        
