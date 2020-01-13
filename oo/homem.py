from oo.pessoa import Pessoa


class Homem(Pessoa):
    pinto = 1
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()# sempre vai chamar o metodo da classe pai no caso pessoa
        return f'{cumprimentar_da_classe}. Aperto de mão'
