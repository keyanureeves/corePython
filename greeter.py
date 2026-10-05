# prompt = "If you share your name, we can personalize the messages you see"
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print(f"\nHello,{name}")

# functions - definng a function
def greet_user():
  """Display a simple greeting"""
  print("Hello")

greet_user()

# passing information into a function
def greet_user(username):
  """Display a simple greeting"""
  print(f"Hello, {username.title()}!")

greet_user('Keyanu')

def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

# This is an infinite loop!
while True:
  print("\nPlease tell me your name:")
  f_name = input("First name")
  l_name = input("Last name")

  formatted_name = get_formatted_name(f_name, l_name)
  print(f"\Hello, {formatted_name}")



