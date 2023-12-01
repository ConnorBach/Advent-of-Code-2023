def solve():
    digits = '1234567890'
    words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    f = open('input.txt')
    ans = 0
    for line in f:
        line = line.strip()
        copy = list(line)
        sum = ''

        for k,v in words.items():
            for i in range(len(line)):
                x = line.find(k, i)
                if x != -1:
                    copy[x] = v
        
        for i in range(len(copy)):
            if copy[i] in digits:
                sum += copy[i]
                break
        for i in range(len(copy)-1, -1, -1):
            if copy[i] in digits:
                sum += copy[i]
                break
        print(line.strip(), ': ', sum)
        ans += int(sum)
    return ans

print(solve())


