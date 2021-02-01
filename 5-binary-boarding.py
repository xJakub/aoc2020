import itertools
import sys
import timeit


def part1(nums):
    print(max(nums))


def part2a(nums):
    num = min(nums) + 1
    while num in nums:
        num += 1
    print(num)


def part2b(nums):
    nums_sorted = sorted(nums)
    part2b_with_sorted(nums_sorted)


def part2b_with_sorted(nums_sorted):
    pos = 0
    while nums_sorted[pos + 1] == nums_sorted[pos] + 1:
        pos += 1
    print(nums_sorted[pos] + 1)


def part2c(nums):
    offset = min(nums)
    visited = [False] * (len(nums) + 1)
    for num in nums:
        visited[num - offset] = True

    print(visited.index(False) + offset)


def sum_0_to_n(n):
    return n * (n + 1) // 2


def part2d(nums):
    nums_min, nums_max = min(nums), max(nums)
    full_sum = sum_0_to_n(nums_max) - sum_0_to_n(nums_min - 1)
    print(full_sum - sum(nums))


def xor_0_to_n(n):
    return [n, 1, n + 1, 0][n % 4]


def part2e(nums):
    nums_min, nums_max = min(nums), max(nums)
    full_xor = xor_0_to_n(nums_max) ^ xor_0_to_n(nums_min - 1)
    actual_xor = 0
    for num in nums:
        actual_xor ^= num
    print(full_xor ^ actual_xor)


def part2f_with_sorted(nums_sorted):
    min_num = nums_sorted[0] + 1
    max_num = nums_sorted[-1] - 1
    offset = nums_sorted[0]  # min(nums)

    while min_num != max_num:
        middle_num = (min_num + max_num) // 2
        expected_pos = middle_num - offset

        if nums_sorted[expected_pos] == middle_num:
            min_num = middle_num + 1
        else:
            max_num = middle_num

    print(min_num)


def main():
    lines = sys.stdin.read().strip().split('\n')
    binary_lines = [line.replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0') for line in lines]
    nums = [int(line, 2) for line in binary_lines]

    calls = [
        (nums, [part1, part2b, part2c, part2d, part2e]),
        (sorted(nums), [part2b_with_sorted, part2f_with_sorted]),
        (nums, [part2a]),
    ]
    for param, functions in calls:
        for function in functions:
            print(f'* Running {function.__name__}')
            start_time = timeit.default_timer()
            function(param)
            elapsed_time = timeit.default_timer() - start_time
            print(f'* {function.__name__} took {elapsed_time:.4f} seconds\n')


main()
