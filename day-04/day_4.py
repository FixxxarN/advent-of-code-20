import re

passports = []

required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

valid_passports = []

extremly_valid_passports = []


def get_value_from_requirement(requirement):
    return passport.split(requirement + ':')[1].split(" ")[0]


def check_if_requirement_is_between_two_numbers(requirement, minValue, maxValue):
    if requirement >= minValue and requirement <= maxValue:
        return True
    else:
        return False


def check_if_hgt_is_valid(hgt):
    if 'cm' in hgt:
        if int(hgt.split('cm')[0]) >= 150 and int(hgt.split('cm')[0]) <= 193:
            return True
        else:
            return False
    elif 'in' in hgt:
        if int(hgt.split('in')[0]) >= 59 and int(hgt.split('in')[0]) <= 76:
            return True
        else:
            return False
    else:
        return False


def check_if_requirement_is_matching_pattern(requirement, pattern):
    pattern = re.compile(pattern)
    if pattern.fullmatch(requirement):
        return True
    else:
        return False


def check_if_ecl_is_valid(ecl):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return any(substring in ecl for substring in valid_ecl)


with open("day-04/input.txt", "r") as filehandler:
    filecontents = filehandler.read().split('\n\n')

    for line in filecontents:
        passports.append(line.replace('\n', ' '))

for passport in passports:
    if all((req in passport) for req in required_fields):
        valid_passports.append(passport)

for passport in valid_passports:
    # if int() >= 1920 and int(passport.split('byr')[1].split(" ")[0]) <= 2002:
    byr = int(get_value_from_requirement('byr'))
    iyr = int(get_value_from_requirement('iyr'))
    eyr = int(get_value_from_requirement('eyr'))
    hgt = get_value_from_requirement('hgt')
    hcl = get_value_from_requirement('hcl')
    ecl = get_value_from_requirement('ecl')
    pid = get_value_from_requirement('pid')

    if check_if_requirement_is_between_two_numbers(byr, 1920, 2002) and check_if_requirement_is_between_two_numbers(iyr, 2010, 2020) and check_if_requirement_is_between_two_numbers(eyr, 2020, 2030) and check_if_hgt_is_valid(hgt) and check_if_requirement_is_matching_pattern(hcl, "#[a-f0-9]{6}") and check_if_ecl_is_valid(ecl) and check_if_requirement_is_matching_pattern(pid, "[0-9]{9}"):
        extremly_valid_passports.append(passport)

# Part 1
print(len(valid_passports))

# Part 2
print(len(extremly_valid_passports))
