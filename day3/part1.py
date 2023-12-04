engine = []
def solve():
    get_input()
    ans = 0
    i = 0
    while i < len(engine):
        j = 0
        while j < len(engine[i]):
            if engine[i][j].isdigit():
                n = get_number(i, j)
                ##print(f'CHECKING: {n} at {i}, {j}')
                if is_adjacent_to_symbol(i, j, len(n)):
                    ##print('ADDING: ', n)
                    ans += int(n) 
                j += len(n)
            j += 1
        i += 1
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
            return True
        elif i-1 >= 0 and j+k < len(engine[i]) and is_symbol(engine[i-1][j+k]):
            #print('up')
            return True
        elif i+1 < len(engine) and j+k+1 < len(engine[i]) and is_symbol(engine[i+1][j+k+1]):
            return True
        elif i+1 < len(engine) and j+k-1 >= 0 and is_symbol(engine[i+1][j+k-1]):
            return True
        elif i-1 >= 0 and j+k+1 < len(engine[i]) and is_symbol(engine[i-1][j+k+1]):
            return True
        elif i-1 >= 0 and j+k-1 >= 0 and is_symbol(engine[i-1][j+k-1]):
            return True

    ends = [j, j+l-1]
    for k in ends:
        #print(f'checking ends: {i}, {k}')
        if k+1 < len(engine[i]) and is_symbol(engine[i][k+1]):
            return True
        elif k-1 >= 0 and is_symbol(engine[i][k-1]):
            return True
    return False

def is_symbol(c):
    if not c.isdigit() and not c == '.':
        return True
    return False

solve()

#get_input()
##print(is_adjacent_to_symbol(5, 9, 2))
