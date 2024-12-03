count = 0
with open('input.txt', 'r') as file:
  for line in file:
    num_strs = line.strip().split(' ')
    nums = list(map(int, num_strs))
    safe: bool = True
    dir: int = 0
    for i in range(1, len(nums)):
      diff = nums[i] - nums[i - 1]
      curr_dir = diff / abs(diff) if diff != 0 else 0
      dir = curr_dir if dir == 0 else dir
      if abs(diff) > 3 or curr_dir == 0 or curr_dir != dir:
        safe = False
        break
    
    if safe:
      count += 1


print(count)

