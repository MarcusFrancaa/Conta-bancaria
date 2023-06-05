class Conta:
    def __init__ (self, num, nome, tipo ):
        self.num_conta=num
        self.saldo_conta=0
        self.status_conta=False
        self.nome_cliente=nome
        self.tipo_conta=tipo
        self.limite=()
        self.limite2=()

    def ativa_conta (self):
        if self.status_conta == False:
            self.status_conta = True
            print(f"A conta foi ativada com sucesso!\n Você já pode depositar, sacar e verificar seu saldo")
        else:
            print("Sua conta já está ativa! \n Você já pode depositar, sacar e verificar seu saldo")

    def ativar_limite(self, quantia_limite):
        self.limite = quantia_limite
        self.limite2 = self.limite

    def depositar(self, quantia_deposito):
        if self.limite2 < self.limite:
            diferenca=self.limite-self.limite2
            if diferenca < quantia_deposito:
                self.saldo_conta= quantia_deposito-diferenca
                self.limite2+=diferenca
                print(f"Você depositou {quantia_deposito} ")
                with open("extrato.txt", 'a', encoding="utf-8") as arquivo:
                    arquivo.write(f"\n Depósito efetuado de {quantia_deposito} reais")
            else:
                self.limite2+=quantia_deposito
                print(f"Você depositou {quantia_deposito}")
                with open("extrato.txt", 'a', encoding="utf-8") as arquivo:
                    arquivo.write(f"\n Depósito efetuado de {quantia_deposito} reais")

    def sacar (self, quantia_saque):
        exc=0
        if self.saldo_conta > 0 and quantia_saque <= self.saldo_conta:
            self.saldo_conta-=quantia_saque
            print(f"Voce sacou {quantia_saque} o saldo da conta é {self.saldo_conta:.2f}")
            with open("extrato.txt", 'a', encoding="utf-8") as arquivo:
                arquivo.write(f"\n Saque efetuado de {quantia_saque} reais")
        elif quantia_saque > self.limite2:
            print(f" Voce tentou sacar {quantia_saque} mas você excedeu seu limite, você so tem {self.limite2} disponível em cheque especial")
        else :
            exc=quantia_saque-self.saldo_conta
            self.limite2 -= exc
            self.saldo_conta=0
            print(f"Você sacou {quantia_saque}")
            with open("extrato.txt", 'a', encoding="utf-8") as arquivo:
                arquivo.write(f"\n Saque efetuado de {quantia_saque} reais")

    def desativar_conta(self):
        if self.saldo_conta == 0 and self.limite2 == self.limite:
            self.status_conta=False
            print(f"A conta agora está desativada")
        elif abs(self.saldo_conta) > 0:
            print(f"Você não pode desativar a conta agora, faça o saque do valor restante! que é {self.saldo_conta:.2f}")
        elif self.limite2 != self.limite:
            diferenca = self.limite - self.limite2
            print(f"Você está com um débito de {diferenca} no seu cheque especial,\n regularize esse débito com um depósito"
                  f" de {diferenca:.2f} reais")
        elif self.status_conta == False:
            print("Sua conta já está desativada")

    def extrato_conta(self):
        with open("extrato.txt", "r", encoding="utf-8") as arquivo:
            extrato = arquivo.read()
        return print("=====Extrato conta=====",extrato)

    def verificar_saldo(self):
        print(f"Seu saldo da conta é {self.saldo_conta:.2f}\n e o seu limite é {self.limite2:.2f}")

c1=Conta(12345,'Marcus', 'Conta corrente')
c2=Conta(4567,'Vitor', 'conta corrente')
c1.ativa_conta()
c1.ativar_limite(500.00)
c1.sacar(20.00)
c1.depositar(50.00)
c1.sacar(300.00)
c1.depositar(150.00)
c1.verificar_saldo()
c1.desativar_conta()
c1.depositar(120.00)
c1.verificar_saldo()
c1.desativar_conta()
print(c1.extrato_conta())
















