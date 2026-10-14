# deleting all instances of sppecific values from a list
pets = [ 'dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
  pets.remove('cat')

print(pets)

# positional arguments
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
# multiple function calls
describe_pet('dog', 'willie')
# keyword arguments
describe_pet(animal_type='rabbit', pet_name= 'Kolo')
describe_pet(pet_name= 'Kolo',animal_type='rabbit')

# default values 
def describe_pet(pet_name, animal_type='dog'):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# describe_pet()

