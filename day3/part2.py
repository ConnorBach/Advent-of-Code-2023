from functools import reduce
engine = []
def solve():
    get_input()
    ans = 0
    i = 0

    gearMap = {}

    while i < len(engine):
        j = 0
        while j < len(engine[i]):
            if engine[i][j].isdigit():
                n = get_number(i, j)
                ##print(f'CHECKING: {n} at {i}, {j}')
                result, gear_i, gear_j = is_adjacent_to_symbol(i, j, len(n))
                if result:
                    ##print('ADDING: ', n)
                    if f'{gear_i}, {gear_j}' in gearMap:
                        gearMap[f'{gear_i}, {gear_j}'].append(int(n))
                    else:
                        gearMap[f'{gear_i}, {gear_j}'] = [int(n)]
                j += len(n)
            j += 1
        i += 1
    print(gearMap)

    for gear, values in gearMap.items():
        if len(values) > 1:
            gearRatio = reduce((lambda x, y: x * y), values)
            ans += gearRatio
    print(ans)

def get_input():
    f = open('input.txt')
    for line in f:
        engine.append(list(line.strip()))

def get_number(i, j):
    line = engine[i]
    left = j
    right = j + 1
    num = ''

    while left >= 0:
        if engine[i][left].isdigit():
            num += engine[i][left]
        else:
            break
        left -= 1

    while right < len(line):
        if engine[i][right].isdigit():
            num += engine[i][right]
        else:
            break
        right += 1
    
    return num

def is_adjacent_to_symbol(i, j, l):
    for k in range(l):
        #print(f'checking: {i}, {j+k}')
        if i+1 < len(engine) and j+k < len(engine[i]) and is_symbol(engine[i+1][j+k]):
            return True, i+1, j+k
        elif i-1 >= 0 and j+k < len(engine[i]) and is_symbol(engine[i-1][j+k]):
            #print('up')
            return True, i-1, j+k
        elif i+1 < len(engine) and j+k+1 < len(engine[i]) and is_symbol(engine[i+1][j+k+1]):
            return True, i+1, j+k+1
        elif i+1 < len(engine) and j+k-1 >= 0 and is_symbol(engine[i+1][j+k-1]):
            return True, i+1, j+k-1
        elif i-1 >= 0 and j+k+1 < len(engine[i]) and is_symbol(engine[i-1][j+k+1]):
            return True, i-1, j+k+1
        elif i-1 >= 0 and j+k-1 >= 0 and is_symbol(engine[i-1][j+k-1]):
            return True, i-1, j+k-1

    ends = [j, j+l-1]
    for k in ends:
        #print(f'checking ends: {i}, {k}')
        if k+1 < len(engine[i]) and is_symbol(engine[i][k+1]):
            return True, i, k+1
        elif k-1 >= 0 and is_symbol(engine[i][k-1]):
            return True, i, k-1
    return False, -1, -1

def is_symbol(c):
    if c == '*':
        return True
    return False

solve()

#get_input()
##print(is_adjacent_to_symbol(5, 9, 2))
