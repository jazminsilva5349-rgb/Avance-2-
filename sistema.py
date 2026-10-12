# 1. Contexto
# Una cuenta bancaria en POO es como un objeto que guarda tu dinero y sabe hacer cosas básicas:
# depositar, retirar o mostrar el saldo. La clase se comporta como algo real y concreto,
# con datos propios y acciones que solo ella puede ejecutar.

# 2. Creación de la Clase Base
class CuentaBancaria:
    # Constructor: inicializa atributos de la clase
    def __init__(self, numero_cuenta, titular, saldo_inicial, tipo):
        self.numero_cuenta = numero_cuenta   # Atributo: número de cuenta
        self.titular = titular               # Atributo: nombre del titular
        self.saldo_inicial = saldo_inicial   # Atributo: saldo inicial
        self.tipo = tipo                     # Atributo: tipo de cuenta (Ahorro, Crédito)

    # Métodos: definen el comportamiento de la clase
    def depositar(self, monto):
        self.saldo_inicial += monto
        print(f"Depósito exitoso de ${monto}. Nuevo saldo: ${self.saldo_inicial}")

    def retirar(self, monto):
        if monto <= self.saldo_inicial:
            self.saldo_inicial -= monto
            print(f"Retiro de ${monto} realizado. Saldo restante: ${self.saldo_inicial}")
        else:
            print(f"Fondos insuficientes. Tu saldo actual es de ${self.saldo_inicial}")

    def consultar_saldo(self):
        print(f"El saldo de la cuenta {self.numero_cuenta} es: ${self.saldo_inicial}")

    def mostrar_info(self):
        print(f"Cuenta: {self.numero_cuenta}, Titular: {self.titular}")
        print(f"Tipo: {self.tipo}, Saldo: ${self.saldo_inicial}")


# 3. Herencia Básica
# Creamos una clase hija que hereda de CuentaBancaria
class CuentaPremium(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo_inicial, tipo, beneficios):
        # Uso de super(): llama al constructor de la clase padre
        super().__init__(numero_cuenta, titular, saldo_inicial, tipo)
        self.beneficios = beneficios

    # Polimorfismo: sobrescribimos el método mostrar_info
    def mostrar_info(self):
        print(f"Cuenta Premium: {self.numero_cuenta}, Titular: {self.titular}")
        print(f"Tipo: {self.tipo}, Saldo: ${self.saldo_inicial}, Beneficios: {self.beneficios}")


# 4. Instanciación y Pruebas
# Objetos de la clase base
cuenta_1 = CuentaBancaria("001", "Ana López", 1500, "Ahorro")
cuenta_2 = CuentaBancaria("002", "Carlos Pérez", 500, "Crédito")

# Objeto de la clase hija (herencia + polimorfismo)
cuenta_premium = CuentaPremium("003", "María Gómez", 3000, "Crédito", "Bonificación anual")

# Acciones con cada objeto
cuenta_1.depositar(500)          # Encapsulamiento: cada objeto maneja su propio estado
cuenta_1.consultar_saldo()

cuenta_2.retirar(200)
cuenta_2.consultar_saldo()

cuenta_premium.depositar(1000)
cuenta_premium.mostrar_info()    # Polimorfismo: método sobrescrito


