# Store information about a pizza being ordered.

pizza = {
  'crust': 'thick',
  'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']} - crust pizza with the following toppings:")

for topping in pizza['toppings']:
  print(f"\t{topping}")

# passing an arbtrary number of arguments
# def make_pizza(*toppings):
#   """Print the list of toppings that have been requested."""
#   print("\nMaking a pizza with the following toppings:")
#   for topping in toppings:
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# mixing positionala and arbtrary number of arguments
def make_pizza(size, *toppings):
  """Summarize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')