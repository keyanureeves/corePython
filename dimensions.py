dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250

# looping through a tuple
for dimension in dimensions:
  print(dimension)

# writing over a tuple
print("Original dimensions:")
for dimension in dimensions:
  print(dimension)

dimensions = (400,100)
print("\nModified dimensions")
for dimension in dimensions:
  print(dimension)
