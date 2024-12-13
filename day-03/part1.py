import re

with open('input.txt') as file:
  content = file.read()

p = re.compile('mul\((\d+),(\d+)\)')
sum: int = 0

for match in p.finditer(content):
  sum += int(match[1]) * int(match[2])

print(sum)