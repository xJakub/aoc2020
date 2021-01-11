import sys


def part1(lines):
    width = len(lines[0])
    path = [line[(3 * y) % width] for y, line in enumerate(lines)]
    print('Part 1:', path.count('#'))


def part2(lines):
    width = len(lines[0])
    product = 1
    for vx, vy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        path = [line[(vx * y) % width] for y, line in enumerate(lines[::vy])]
        product *= path.count('#')
    print('Part 2:', product)


def main():
    lines = sys.stdin.read().strip().split('\n')
    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
