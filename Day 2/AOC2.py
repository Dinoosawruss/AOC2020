def main():
    f = open("./db.txt", "r")
    db = [line.strip() for line in f.readlines()]

    print(part1(db))
    print(part2(db))

def part1(db):
    validCount = 0
    for line in db:
        words = line.split()

        _min,_max = map(int, words[0].split('-'))
        letter = words[1][0]

        password = words[2]

        if _min <= password.count(letter) <= _max:
            validCount += 1

    return validCount

def part2(db):
    validCount = 0
    for line in db:
        words = line.split()

        pos1, pos2 = map(int, words[0].split('-'))
        letter = words[1][0]

        password = words[2]

        if bool(password[pos1-1] == letter) ^ bool(password[pos2-1] == letter):
            validCount += 1

    return validCount

main()
