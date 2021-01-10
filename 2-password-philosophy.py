import sys, re


def parse_line_with_split(line):
    num1_str, num2_str = line.split(' ')[0].split('-')
    letter = line.split(' ')[1].split(':')[0]
    word = line.split(' ')[2]
    return int(num1_str), int(num2_str), letter, word


def parse_line_with_regex(line):
    match = re.search(r"^(\d+)-(\d+) (\w): (\w+)$", line)
    num1_str, num2_str, letter, word = match.groups()
    return int(num1_str), int(num2_str), letter, word


def is_password_valid_part1(case):
    min_times, max_times, letter, password = case
    return min_times <= password.count(letter) <= max_times


def is_password_valid_part2a(case):
    pos1, pos2, letter, password = case
    return (password[pos1 - 1] + password[pos2 - 1]).count(letter) == 1


def is_password_valid_part2b(case):
    pos1, pos2, letter, password = case
    return (password[pos1 - 1:pos1] + password[pos2 - 1:pos2]).count(letter) == 1


def parse_lines(lines):
    cases_with_split = [parse_line_with_split(line) for line in lines]  # list(map(parse_line_with_split, lines))
    cases_with_regex = [parse_line_with_regex(line) for line in lines]
    assert (cases_with_split == cases_with_regex)
    return cases_with_regex


def part1(cases):
    # len(list(filter(is_password_valid_part1, cases))
    valid_cases = [case for case in cases if is_password_valid_part1(case)]
    print('Part 1:', len(valid_cases))


def part2a(cases):
    try:
        # this solution can fail if we specify out-of-bounds positions
        valid_cases = [case for case in cases if is_password_valid_part2a(case)]
        print('Part 2a:', len(valid_cases))
    except IndexError as e:
        print(e)


def part2b(cases):
    valid_cases = [case for case in cases if is_password_valid_part2b(case)]
    print('Part 2b:', len(valid_cases))


def main():
    lines = sys.stdin.read().strip().split('\n')
    cases = parse_lines(lines)

    part1(cases)
    part2a(cases)
    part2b(cases)


if __name__ == '__main__':
    main()
