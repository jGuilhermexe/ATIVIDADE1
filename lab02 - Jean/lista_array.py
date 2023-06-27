from estrutura_elementar import estrutura_elementar

class ArrayList(estrutura_elementar):
    def __init__(self):
        self.lista = []

    def esta_vazio(self) -> bool:
        if len(self.lista) == 0:
            return True
        return False
    
    def inserir(self, item):
        self.lista.append(item)

    def remove(self, item):
        self.lista.remove(item)

    def tamanho(self) -> int:
        return len(self.lista)

    def limpa(self):
        self.lista.clear()

    def procura(self, item) -> bool:
        for i in self.lista:
            if (i == item):
                return True
        return False

    def indice_de(self, item):
        if item in self.lista:
            return self.lista.index(item)
        else:
            return -1

    def recupera_indice(self, index):
        if 0 <= index < len(self.lista):
            return self.lista[index]
        else:
            return None