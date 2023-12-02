
def solve():
    f = open('input.txt')
    ans = 0

    for line in f:
        vals = {
            'red': 0,
            'green': 0,
            'blue': 0 
        }

        s = line.strip().split(':')
        gameNumber = s[0].split(' ')[1]
        cubes = s[1]

        games = cubes.split(';')
        useGame = True
        for game in games:
            blocks = [x.strip() for x in game.split(',')]
            for block in blocks:
                s = block.split()
                curNum = int(s[0])
                color = s[1]
                if curNum > vals[color]:
                    vals[color] = curNum

        print(vals)
        p = 1
        for k,v in vals.items():
            p *= v
        ans += p
    return ans

print(solve())


