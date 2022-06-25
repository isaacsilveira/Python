#altura da parede
altura_da_parede = float(input('digite a altura da parede:'))
#largura da parede
largura_da_parede = float(input('digite a largura da parede:'))
# dimensao da parede area e quantos litros vai precisar
area_da_parede= float(altura_da_parede*largura_da_parede)
# a cada 2m quadrados gasta 2 litros de tinta
tinta_litros = float(area_da_parede/2*2)
print(f'sua parede tem dimenssão de {largura_da_parede}X{altura_da_parede}, area de {area_da_parede}m² ')
print(f'para printar a parede será necessario {tinta_litros}L de tinta ') 
 