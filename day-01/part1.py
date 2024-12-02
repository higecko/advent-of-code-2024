from typing import List
a: List[int] = []
b: List[int] = []

with open('input.txt', 'r') as puzzle_input:
  for line in puzzle_input:
    strA, strB = line.strip().split('   ')
    a.append(int(strA))
    b.append(int(strB))

a.sort()
b.sort()

distance_sum = 0

for intA, intB in zip(a, b):
  distance_sum += abs(intA - intB)

print(f'Sum of distances is {distance_sum}')