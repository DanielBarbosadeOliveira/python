class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
        
    def Depositar(self, valor):
         self._saldo += valor
    
    def Sacar(self, valor):
        self._saldo -= valor
    
    def mostrar_saldo(self, valor):
        return self._saldo
    
     
    
