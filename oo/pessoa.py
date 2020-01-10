class Pessoa():
    olhos=2 #atributo default ou atributo de classe


    def __init__(self,*filhos, nome=None, idade=35):#seria o moetodo contrutor. nome do parametro caso
        self.idade = idade
        self.nome=nome
        self.filhos=list(filhos)


    def cumprimentar(self):
        return 'oi'