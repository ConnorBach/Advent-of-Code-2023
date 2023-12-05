def get_input():
    lines = []
    f = open('input.txt')
    for line in f:
        lines.append(line)
    return lines

def get_copies(card, cards):
    #print('checking: ', card.split(':')[0].strip())
    cur = int(card.split(':')[0].split(' ')[-1])
    
    nums = card.split(':')[1]
    winning_nums = nums.split('|')[0].strip().split(' ')
    my_nums = nums.split('|')[1].strip().split(' ')

    winning_nums = set([x for x in winning_nums if x != ''])
    my_nums = [x for x in my_nums if x != '']

    pts = 0
    matches = 0
    for n in my_nums:
        if n in winning_nums:
            matches += 1

    #print('matches: ', matches)
    if matches > 0:
        pts = 1
        for i in range(matches):
            pts += get_copies(cards[cur + i], cards)
        return pts
    return 1

def solve():
    ans = 0
    cards = get_input()

    cardNum = 1
    for card in cards:
        ans += get_copies(card, cards)

    print(ans)
solve()