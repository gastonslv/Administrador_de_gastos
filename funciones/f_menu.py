def menu_principal(fondos, ahorros):
    """"
    Despliega un menu de opciones, y retorna la opcion seleccionada
    por el usuario.
    """

    salir = False
    decision_usuario = 0

    while salir == False:
        try:
            print("//////////////////////")
            print("\nFondos:  $" + str(fondos[0]) + "\n" +
                  "Ahorros: $" + str(ahorros[0]) + "\n\n" +
                  "Menu de opciones: \n\n" +
                  "\t1.Gastos\n" +
                  "\t2.Ingresos\n" +
                  "\t3.Ahorrar\n" +
                  "\t4.Movimientos\n" +
                  "\t5.Salir\n")
            decision_usuario = int(input("Seleccione una opcion: "))
        except ValueError:
            print("\n--------Error--------")
            print("El valor que ingreso es incorrecto, vuelava a intentarlo")
            print("---------------------\n")
            continue
        else:
            if (decision_usuario < 1) or (decision_usuario > 5):
                print("\n--------Error--------")
                print("Debe seleccionar una opcion entre 1 y 5, vuelva a intentarlo")
                print("---------------------\n")
            else:
                salir = True

    return decision_usuario
            

