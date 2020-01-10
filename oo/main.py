from oo.pessoa import Pessoa


caio=Pessoa(nome='Caio')
max=Pessoa(caio ,nome='Max')
print(Pessoa.cumprimentar(caio))
print(caio.nome)
print(max.nome)
print(max.idade)

for filho in max.filhos:
    print(filho.nome)
max.sobrenome='Wesley'
del max.filhos
print(max.__dict__)
print(caio.__dict__)