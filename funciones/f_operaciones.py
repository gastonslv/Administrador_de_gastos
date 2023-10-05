def calcular_gastos(fondos, gastos, movimientos):
    """
    Le pide al usuario que ingrese su gasto. La funcion se encarga de descontar
    del fondo dicho gasto y registrar la operacion en 'gastos' y 'movimientos'.
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
    """
    Le pide al usuario el ingreso de dinero a la cuenta. La funcion se encarga de agregar
    al fondo dicho ingreso y registrar la operacion en 'ingresos' y 'movimientos'.
    """
    salir = False
    ingreso = {}
    descripcion = '-'
    fecha = ''

    while salir == False:
        try:
            monto_ingreso = float(input("Ingrese el monto: "))
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

def calcular_ahorro(fondos, ahorros, movimientos):
    """
    Mueve dinero desde los fondos a los ahorros, y registra la operacion
    en movimientos.
    """
    salir = False 
    mover_fondos = 0
    ahorro = {}
    descripcion = ''
    fecha = ''

    while salir == False:
        try:
            mover_fondos = float(input("Ingrese la cantidad de dinero que quiero ahorrar: "))
            if mover_fondos > fondos[0]:
                print("No hay fondos suficientes para realizar la operacion!")
                print("Vuelva a intentarlo...\n")
                continue
            else:
                fondos[0] -= mover_fondos
                ahorros[0] += mover_fondos
                descripcion = input("Breve descripcion: ")
                fecha = input("Fecha: ")
                ahorro = {
                    'tipo': 'ahorro',
                    'monto': mover_fondos,
                    'resumen': descripcion,
                    'fecha': fecha,
                }
                movimientos.append(ahorro)
                salir = True
        except ValueError:
            print("\n--------Error--------")
            print("El valor que ingreso es incorrecto, vuelava a intentarlo")
            print("---------------------\n")
            continue
    return 0