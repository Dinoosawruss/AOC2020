import re

def main():
    f = open('inp.txt', 'r')
    inp = [l.strip() for l in f.read().split('\n')]

    print(part1(inp))
    print(part2(inp))

def part1(inp):
    total = 0
    
    validKeys = ['byr', 'iyr', 'eyr','hgt','hcl','ecl','pid']
    passports = {}
    
    for line in inp:
        if line != "":
            for keyValuePair in line.split():
                key, value = keyValuePair.split(":")

                passports[key] = value

        else:
            valid = True

            for key in validKeys:
                if key not in passports.keys():
                    valid = False

            if valid:
                total += 1

            passports = {}

    return total

def part2(inp):
    total = 0
    
    passports = {}
    for line in inp:
        if line != "": 
            for keyValuePair in line.split():
                key, value = keyValuePair.split(":")
                passports[key] = value
                
        else: 
            for x in ['byr','iyr','eyr']:
                if x not in passports.keys():
                    passports[x] = -1
                    
            for x in ['hgt','hcl','ecl','pid']:
                if x not in passports.keys():
                    passports[x] = ''
                    
            if 1920 <= int(passports['byr']) <= 2002 and\
                    2010 <= int(passports['iyr']) <= 2020 and\
                    2020 <= int(passports['eyr']) <= 2030 and\
                    (\
                        (passports['hgt'][-2:] == 'cm' and 150 <= int(passports['hgt'][:-2]) <= 193) or \
                        (passports['hgt'][-2:] == 'in' and 59  <= int(passports['hgt'][:-2]) <= 76)\
                    ) and\
                    re.match('^\\#[0-9a-f]{6}$', passports['hcl']) and\
                    passports['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and\
                    re.match('^[0-9]{9}$', passports['pid']):
                total += 1
                
            passports = {}
            
    return total

            
    

main()
