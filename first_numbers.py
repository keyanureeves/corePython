# using the range function
for value in range(1, 5):
  print(value)


# for value in range(1, 6):
#   print(value)


# for value in range(6):
#   print(value)

# list() can be used to convert that same set into a list
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
  square = value ** 2
  squares.append(square)

print(squares)

# to write this code more concisely
squares = []
for value in range(1,11):
  squares.append(value ** 2)

print(squares)

# list comprehensions 
squares = [value ** 2 for value in range(1,11)]
print(squares)