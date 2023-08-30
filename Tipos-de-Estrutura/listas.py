# primeiro criamos a lista com o class
class Lista:
    def __init__(self, maxnelems):
        self.dados = [0] * maxnelems
        self.nelems = 0

# agora vamos criar a função consulta

def consulta (self, x):
    i = 0
    while (i < self.nelems) and (self.dados[i]!=x):
        i += 1
    if (i < self.nelems):
        return True
    return False