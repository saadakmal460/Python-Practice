pizza = ['Tikka' , 'Fajita' , 'Peporoni' , 'Peri Peri']

friend_pizza = pizza[:]

pizza.append('Vegi')

friend_pizza.append('Salsa')

for i in pizza:
    print(f'My pizza {i}')
    
for i in friend_pizza:
    print(f'Friend pizza {i}')
    