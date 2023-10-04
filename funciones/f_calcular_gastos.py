def calcular_gastos(fondos, gastos, movimientos):
    salir = False
    gasto = {}
    descripcion = '-'
    fecha = ''

    while salir == False:
        try:
            monto_gasto = float(input("Ingrese el monto del gasto: "))
            if monto_gasto > fondos[0]: # verificamos que hayan fondos
                print("No hay fondos suficientes para realizar la operacion.")
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


        
