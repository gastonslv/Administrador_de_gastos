def menu_principal():
    """"
    Despliega un menu de opciones, y retorna la opcion seleccionada
    por el usuario.
    """

    salir = False
    decision_usuario = 0

    while salir == False:
        try:
            print("\nMenu de opciones: \n\n" +
                  "\t1.Gastos\n" +
                  "\t2.Ingresos\n" +
                  "\t3.Ahorros\n" +
                  "\t4.Consultar fondos\n")
            decision_usuario = int(input("Seleccione una opcion: "))
        except ValueError:
            print("\n--------Error--------")
            print("El valor que ingreso es incorrecto, vuelava a intentarlo")
            print("---------------------\n")
            continue
        else:
            if (decision_usuario < 1) or (decision_usuario > 4):
                print("\n--------Error--------")
                print("Debe seleccionar una opcion entre 1 y 4, vuelva a intentarlo")
                print("---------------------\n")
            else:
                salir = True

    return decision_usuario
            

