class Espaco:
    def __init__(self):
        self.__nome: str = "empty"
        self.__qtd: int = 0
        self.__preco: float = 0.0

    def getNome(self):
        return self.__nome  # Retorna o nome

    def setNome(self, n: str):
        self.__nome = n  # Colocar o nome
        return self.__nome

    def getQtd(self):
        return self.__qtd  # retorna Quantidade

    def setQtd(self, q: int):
        self.__qtd = q
        return self.__qtd

    def getPreco(self):
        return self.__preco  # retorna preço

    def setPreco(self, p: int):
        self.__preco = p
        return self.__preco

    def __str__(self):
        return f"[ {self.getNome():>7} : {self.getQtd()} U : {self.getPreco():.2f} RS]"


class Maquina:
    def __init__(self, capacidade: int):
        self.capacidade: int = capacidade
        self.slot: list[Espaco | None] = []
        self.saldo: float = 0

        for _ in range(capacidade):
            self.slot.append(Espaco())

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, valor: int):
        self.saldo += valor
        return

    def setSlot(self, indice: int, nome: str, qtd: int, preco: float):
        if indice < 0 or indice > self.capacidade:
            print("fail: indice nao existe")
            return
        self.slot[indice].setNome(nome)
        self.slot[indice].setQtd(qtd)
        self.slot[indice].setPreco(preco)

    def limpar(self, indice: int):
        if indice < 0 or indice > self.capacidade:
            print("fail: indice nao existe")
            return
        n: str = "empty"
        self.slot[indice].setNome(n)
        self.slot[indice].setQtd(0)
        self.slot[indice].setPreco(0)

    def pedirTroco(self):
        troco = self.saldo
        self.saldo = 0
        print(f"voce recebeu{troco: .2f} RS")
        return troco

    def comprar(self, ind: int):
        if ind < 0 or ind > self.capacidade:
            print("fail: indice nao existe")
            return

        s = self.slot[ind]

        if self.slot[ind] is None:
            print("fail: espiral sem produtos")
            return

        if self.saldo < s.getPreco():
            print("fail: saldo insuficiente")
            return

        if s.getQtd() <= 0:
            print("fail: espiral sem produtos")
            return
        s.setQtd(s.getQtd() - 1)
        self.saldo -= s.getPreco()
        print(f"voce comprou um {s.getNome()}")

    def __str__(self):
        saida = f"saldo:{self.getSaldo(): .2f}\n"
        for i, s in enumerate(self.slot):
            saida += f"{i} {s}\n"
        return saida.strip()


def main():
    maquina: Maquina | None = None
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        if args[0] == "init":
            c = int(args[1])
            maquina = Maquina(c)
        if args[0] == "show":
            print(maquina)
        if args[0] == "set":
            indice = int(args[1])
            nome = str(args[2])
            qtd = int(args[3])
            preco = float(args[4])
            maquina.setSlot(indice, nome, qtd, preco)
        if args[0] == "limpar":
            ind = int(args[1])
            maquina.limpar(ind)
        if args[0] == "dinheiro":
            valor = int(args[1])
            maquina.setSaldo(valor)
        if args[0] == "troco":
            maquina.pedirTroco()
        if args[0] == "comprar":
            ind = int(args[1])
            maquina.comprar(ind)


main()
