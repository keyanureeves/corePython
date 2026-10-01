bicycles = ['trek', 'cannondable', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"my first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = [ 'honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# append method
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# inserting elements into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements from a list
motorcycles = [ 'honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

colors = ['orange', 'blue', 'purple']
print(colors)

popped_color = colors.pop()
print(colors)
print(popped_color)

motorcycles = [ 'honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was {last_owned.title()}")

motorcycles = [ 'honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}")

# removing an item by value
motorcycles = [ 'honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = [ 'honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

















