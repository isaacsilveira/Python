#cambio 03/05/2022 
#Dolar         4.98
#Euro          5,22
#Libra         6,20
#Bitcon BTC 189,870
#Ethereum    14,030

#quanto voce tem na carteira? R$
#com esse dinhero voce pode comprar resposta_1 
#com esse dinhero voce pode comprar resposta_2
#com esse dinhero voce pode comprar resposta_3
#com esse dinhero voce pode comprar resposta_4
#com esse dinhero voce pode comprar resposta_5

carteira=float(str(input('quanto voce tem na carteira? R$')))

resposta_1=float(round(carteira/4.98))
resposta_2=float(round(carteira/5.22))
resposta_3=float(round(carteira/6.20))
resposta_4=float(carteira/189870)
resposta_5=float(carteira/14030)

print(f'com esse dinhero voce pode comprar {resposta_1} em Dolares') 
print(f'com esse dinhero voce pode comprar {resposta_2} em Euros')
print(f'com esse dinhero voce pode comprar {resposta_3} em Libras')
print(f'com esse dinhero voce pode comprar {resposta_4} em BTC')
print(f'com esse dinhero voce pode comprar {resposta_5} em ETH')