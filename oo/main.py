from oo.pessoa import Pessoa
from oo.homem import Homem
from oo.Mutantes import Mutantes


caio=Mutantes(nome='Caio')
max=Homem(caio ,nome='Max')

print(Pessoa.cumprimentar(caio))
print(caio.nome)
print(max.nome)
print(max.idade)
max.olhos=1# posso trocar na classe principal diretamente
for filho in max.filhos:
    print(filho.nome)
max.sobrenome='Wesley'
del max.filhos
print(max.__dict__)
print(caio.__dict__)
Pessoa.olhos=3
print(Pessoa.olhos)
print(max.olhos)
print(id(Pessoa.olhos), id(max.olhos), id(caio.olhos))
print(Pessoa.metodo_estatico(), max.metodo_estatico())
print(Pessoa.nome_e_atruibutos_de_clases() )
print(f'Caio vai ter {caio.olhos} Olhos, vai ter {caio.orelha} orelhas e vai ter {caio.chife} chife')
print(f'Max vai ter {max.olhos} olhos, {max.orelha} orelhas e {max.pinto} pinto')

print(caio.cumprimentar())
print(max.cumprimentar())
