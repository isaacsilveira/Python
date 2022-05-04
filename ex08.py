#tabela de convercao 
#km /1000
#hm /100
#dam /10
#numero em metro 0
#dm *10
#cm *100
#mm *1000

metro=int(input('Digite um numero em metros:'))
km=float(metro /1000)
hm=float(metro /100)
dam=float(metro /10)
dm=float(metro *10)
cm=float(metro*100)
mm=float(metro*1000)

print(f'seu numero em quilometros :{km}')
print(f'seu numero em hectrometros:{hm}')
print(f'seu numero em decametros  :{dam}')
print(f'seu numero em decimetros  :{dm}')
print(f'seu numero em centimetros :{cm}')
print(f'seu numero em milimetros  :{mm}')