# tipo pilha é como uma lista lifo (last in first out)

# criando a pilha
class Pilha:
    def __init__ (self, maxnelems):
        self.dados = {0} * maxnelems
        self.nelems = 0

# criando função empilha
def empilha (self, x):
    if(self.nelems == len(self.dados)):
        return False
    self.dados[self.nelems] = x
    self.nelems += 1
    return True