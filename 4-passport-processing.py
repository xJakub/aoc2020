import re
import sys


def parse_case(text):
    pairs = re.findall(r"(\w+):([^\s]+)", text)
    return {key: val for key, val in pairs}


def is_passport_valid_part1(case):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return all(key in case for key in required_keys)  # required_keys.issubset(case.keys())


def part1(cases):
    print('Part 1:', len([case for case in cases if is_passport_valid_part1(case)]))


def is_passport_valid_part2(case):
    regexes = {
        'byr': r'^(19[2-9][0-9]|200[0-2])$',  # 1920-2002
        'iyr': r'^(20(1[0-9]|20))$',  # 2010-2020
        'eyr': r'^(20(2[0-9]|30))$',  # 2020-2030
        'hgt': r'^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$',  # 150-193cm / 59-76in
        'hcl': r'^(#[0-9a-f]{6})$',  # hex color
        'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
        'pid': r'^([0-9]{9})$',
    }
    return all(key in case and re.search(regex, case[key]) for key, regex in regexes.items())


def part2(cases):
    print('Part 2:', len([case for case in cases if is_passport_valid_part2(case)]))


def main():
    case_texts = sys.stdin.read().strip().split('\n\n')
    cases = [parse_case(text) for text in case_texts]
    part1(cases)
    part2(cases)


if __name__ == '__main__':
    main()
