import random
import sys

length = int(sys.argv[1])

nums = list(range(1, length))
offset = random.randint(0, length)

random.shuffle(nums)
nums = nums[:-1] + [0, length]
random.shuffle(nums)

nums = [num + offset for num in nums]

max_binary_length = len(f'{max(nums):b}')
for num in nums:
    num_binary = f'{num:b}'.zfill(max_binary_length)
    num_binary_part1 = num_binary[:-3].replace('1', 'B').replace('0', 'F')
    num_binary_part2 = num_binary[-3:].replace('1', 'R').replace('0', 'L')
    print(num_binary_part1 + num_binary_part2)
