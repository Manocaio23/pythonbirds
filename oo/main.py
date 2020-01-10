from oo.pessoa import Pessoa


caio=Pessoa(nome='Caio')
max=Pessoa(caio ,nome='Max')
print(Pessoa.cumprimentar(caio))
print(caio.nome)
print(max.nome)
print(max.idade)

for filho in max.filhos:
    print(filho.nome)

