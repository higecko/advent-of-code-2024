from typing import List, Dict

left: List[int] = []
right: List[int] = []

with open('input.txt', 'r') as puzzle_input:
  for line in puzzle_input:
    strA, strB = line.strip().split('   ')
    left.append(int(strA))
    right.append(int(strB))

frequencies: Dict[int, int] = {}

for num in right:
  if num in frequencies:
    frequencies[num] += 1
  else:
    frequencies[num] = 1

score_sum = 0

for num in left:
  score = frequencies.get(num, 0)
  score_sum += num * score

print(f'Sum of scores is {score_sum}')