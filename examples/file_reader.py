# from pathlib import Path

# path = Path(__file__).parent/'pi_digits.txt'
# contents = path.read_text()
# print(contents)

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
pi_string = ''
for line in lines:
  pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

