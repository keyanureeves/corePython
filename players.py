players = ['charles', 'martina', 'michael', 'florence', 'eli']
# slicing a list
print(players[0:3])
print(players[1:4]) 
print(players[:4])
print(players[2:])

# looping through a slice 
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())
