vals = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solve():
    f = open('input.txt')
    ans = 0

    for line in f:
        s = line.strip().split(':')
        gameNumber = s[0].split(' ')[1]
        cubes = s[1]

        games = cubes.split(';')
        useGame = True
        for game in games:
            blocks = [x.strip() for x in game.split(',')]
            if not check_game(blocks):
                useGame = False

        if useGame:
            ans += int(gameNumber)
    return ans

def check_game(blocks):
    for block in blocks:
        if vals[block.split()[1]] < int(block.split()[0]):
            return False
    return True

print(solve())


