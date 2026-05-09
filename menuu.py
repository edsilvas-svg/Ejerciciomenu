while True:
    print("--MENU--")
    print("1 PAGO TARHETA De creditio")
    print("2 simulacion de comppra")
    print("3 salir")

    op = int(input("ingrese su opcion: "))

    if op == 1:
        print("pagando")
    elif op == 2:
        print("comprando")
    elif op == 3:
        print("saliendo")
        break
    else:
        print("invalido")
