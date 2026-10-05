def build_person(first_name, last_name, age = None):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  if age:
    person['age'] = age
  return person

musician = build_person('keyanu', 'reeves', 25)
print(musician)

mnisa = build_person('stv', 'koker')
print(mnisa)
# age can be updated later