# tipo pilha é como uma lista lifo (last in first out)

# criando a pilha
class Pilha:
    def __init__ (self, maxnelems):
        self.dados = {0} * maxnelems
        self.nelems = 0

# criando função empilha (push)
def empilha (self, x):
    if(self.nelems == len(self.dados)):
        return False
    self.dados[self.nelems] = x
    self.nelems += 1
    return True

# criando função desempilha (pop)
def desempilha (self):
    if(self.nelems == 0):
        return (False, -1)
    x = self.dados[self.nelems - 1]
    self.nelems -=1
    return (True, x)