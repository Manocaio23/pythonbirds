class Pessoa():
    olhos=2 #atributo default ou atributo de classe
    orelha=2


    def __init__(self,*filhos, nome=None, idade=35):#seria o moetodo contrutor. nome do parametro caso
        self.idade = idade
        self.nome=nome
        self.filhos=list(filhos)


    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atruibutos_de_clases(cls): #pode acessar os atributos da classe no caso olhos da classe e orelhas
        return f'{cls} - olhos {cls.olhos} e orelhas {cls.orelha}'