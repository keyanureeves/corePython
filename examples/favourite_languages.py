favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through all the keys in dictionary

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
}

for name in favorite_languages.keys():
  print(name.title())

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(f"Hi {name.title()}.")

  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!")

# looping thru a dictionarys keys in a particular order
for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")


# looping through all values in a dictionary looping through a set

print("The following languages have been mentions:")
for language in set(favorite_languages.values()):
  print(language)

# A list in a dictionary
# Store information about a pizza being ordered.
favorite_languages = {
  'jen': ['python', 'rust'],
  'sarah': ['c'],
  'edward': ['rust', 'go'],
  'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
  print(f"\n{name.title()}'s favorite languages are:")
  for language in languages:
    print(f"\t{language.title()}")





