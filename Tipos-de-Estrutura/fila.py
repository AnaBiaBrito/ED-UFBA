# criar fila

class Pilha:
    def __init__ (self, maxelems):
        self.dados = [0] * maxelems
        self.prim = 0
        self.nelems = 0

# enfileirar

def enfileirar (self, x):
    if(len(self.dados)) == self.nelems:
        return False
    self.dados[self.nelems] = x
    self.nelems += 1
    return True

# desenfileirar