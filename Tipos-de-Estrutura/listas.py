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
#se nao for encontrado o elemento, i terá o tamanho da lista, caso contrário, i será maior.

# função insere
def insere (self, x):
    if(self.consulta(x)) or self.nelems == len(self.dados):
        return False
    
    self.dados[self.nelems] = x #aqui ele insere x no primeiro espaço vazio da lista.
    self.nelems += 1
    return True

# função remove (diminuindo a lista, para casos onde a ordem não é importante, caso seja importante, seria necessario copiar valor por valor para a posição anterior)(aqui ele pede para fazer considerando que a funçao consulta retorne, além de True, também a posição de x (breve tentarei fazer a alteração que permite isso))
def remove (self, x):
    res, i = self.consulta(x)

    if (not res):
        return False
    self.nelems -= 1
    self.dados[i] = self.dados[self.nelems]
    return True

