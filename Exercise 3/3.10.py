cities = ['Lahore' , 'Karachi' , 'Islamabad' , 'Multan' , 'Gujranwala']


cities.append('Okara')

cities.insert(2 , 'Faislabad')

cities.pop()
cities.pop(1)

cities.remove('Islamabad')

del cities[1]

print(cities)

print(sorted(cities))
print(sorted(cities , reverse=True))


cities.reverse()
print(cities)

print(len(cities))
