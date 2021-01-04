import itertools
import sys
import timeit


def part1a(nums, target):
    for a, b in itertools.combinations(nums, 2):
        if a + b == target:
            print(f'{a}*{b} = {a * b}')


def part1b(nums, target):
    if min(nums) < 0:  # don't run this with negative numbers!
        print('Found negative numbers, skipping!')
        return

    visited = [False] * (target + 1)
    for a in nums:
        if a <= target:
            b = target - a
            if visited[b]:
                print(f'{a}*{b} = {a * b}')
            visited[a] = True


def part1c(nums, target):
    visited = set()
    for a in nums:
        b = target - a
        if b in visited:
            print(f'{a}*{b} = {a * b}')
        visited.add(a)


def part1d(nums, target):
    nums_sorted = sorted(nums)
    b_pos = len(nums_sorted) - 1
    for a_pos, a in enumerate(nums_sorted):
        while b_pos > a_pos and a + nums_sorted[b_pos] >= target:
            b = nums_sorted[b_pos]
            if a + b == target:
                print(f'{a}*{b} = {a * b}')
            b_pos -= 1


def part2a(nums, target):
    for a, b, c in itertools.combinations(nums, 3):
        if a + b + c == target:
            print(f'{a}*{b}*{c} = {a * b * c}')


def part2b(nums, target):
    if min(nums) < 0:  # don't run this with negative numbers!
        print('Found negative numbers, skipping!')
        return

    visited = [False] * (target + 1)
    for a_pos, a in enumerate(nums):
        if a <= target:
            for c_pos in range(a_pos + 1, len(nums)):
                c = nums[c_pos]
                b = target - a - c
                if b >= 0 and visited[b]:
                    print(f'{a}*{b}*{c} = {a * b * c}')
            visited[a] = True


def part2c(nums, target):
    visited = set()
    for a_pos, a in enumerate(nums):
        for c_pos in range(a_pos + 1, len(nums)):
            c = nums[c_pos]
            b = target - a - c
            if b in visited:
                print(f'{a}*{b}*{c} = {a * b * c}')
        visited.add(a)


def part2d(nums, target):
    nums_sorted = sorted(nums)
    for c_pos, c in enumerate(nums_sorted):
        b_pos = len(nums_sorted) - 1
        for a_pos in range(c_pos + 1, len(nums_sorted)):
            a = nums_sorted[a_pos]
            while b_pos > a_pos and a + c + nums_sorted[b_pos] >= target:
                b = nums_sorted[b_pos]
                if a + b == target - c:
                    print(f'{a}*{b}*{c} = {a * b * c}')
                b_pos -= 1


def main():
    target = 2020
    lines = sys.stdin.read().strip().split('\n')
    nums = [int(line) for line in lines]  # list(map(int, lines))

    functions = [part1a, part1b, part1c, part1d, part2b, part2c, part2d, part2a]
    for function in functions:
        print(f'* Running {function.__name__}')
        start_time = timeit.default_timer()
        function(nums, target)
        elapsed_time = timeit.default_timer() - start_time
        print(f'* {function.__name__} took {elapsed_time:.4f} seconds\n')


main()
