def main():
    f = open('inp.txt', 'r')
    inp = [line.strip() for line in f.readlines()]
    print(part1(inp))
    print(part2(inp))

def checkEncounters(inp, xMove, yMove):
    total = 0
    x, y = 0, 0

    while y < len(inp):
        line = inp[y]

        if line[x % len(line)] == "#":
            total += 1

        x += xMove
        y += yMove

    return total

def part1(inp):
    return checkEncounters(inp, 3, 1)

def part2(inp):
    moves = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    out = 1
    
    for move in moves:
        out *= checkEncounters(inp, move[0], move[1])

    return out

main()
