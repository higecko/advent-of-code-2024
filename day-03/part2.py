import re

with open('input.txt') as file:
  content = file.read()

p = re.compile('mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)')
sum: int = 0
enabled = True
for match in p.finditer(content):
  if match[0].startswith('mul') and enabled:
    sum += int(match[1]) * int(match[2])
  else:
    enabled = match[0] == "do()"

print(sum)