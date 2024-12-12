class bank:
    def __init__(self):
        self.numero_cuenta=""
        self.saldo=0.0

    def depositar(self,cantidad):
        self.saldo += cantidad
        print(f"Deposito Exitoso! \n"
              f"Nuevo saldo ${self.saldo}")

    def retirar(self,cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= cantidad
            print(f"Retiro Exitoso! \n"
                  f"Nuevo saldo ${self.saldo}")


banco = bank()
banco.numero_cuenta = "544864445"
banco.saldo= int(input("Ingrese su sado inicial: ->$ "))

opcion = None

while opcion != 3:
    print("""
    1) Desea Depositar Dinero en cuenta?
    2) Desea Retirar Dinero de su cuenta?
    3) Salir
    """)
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        banco.depositar(int(input("Ingrese cuanto desea ingresar? ->$ ")))
    elif opcion == 2:
        banco.retirar(int(input("Cuanto desea Retirar? ->$ ")))
    elif opcion == 3:
        print("Gracias por usar nuestros servicios")
