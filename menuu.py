saldo = 100000

while True:
    print("--MENU--")
    print("1 PAGO TARHETA De creditio")
    print("2 simulacion de comppra")
    print("3 salir")

    op = int(input("ingrese su opcion: "))

    if op == 1:
        print("pagando")
        montopagar = int(input("Ingrese monto a pagar: "))
        if montopagar >= 0:
            if montopagar <= saldo:
                saldo = saldo - montopagar
                print("el saldo es : ",saldo)

    elif op == 2:
        print("comprando")
    elif op == 3:
        print("saliendo")
        break
    else:
        print("invalido")
