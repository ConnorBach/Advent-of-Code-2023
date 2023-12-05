def get_input():
    lines = []
    f = open('input.txt')
    for line in f:
        lines.append(line)
    return lines


def solve():
    ans = 0
    cards = get_input()

    cardNum = 1
    for card in cards:
        nums = card.split(':')[1]
        winning_nums = nums.split('|')[0].strip().split(' ')
        my_nums = nums.split('|')[1].strip().split(' ')

        winning_nums = set([x for x in winning_nums if x != ''])
        my_nums = [x for x in my_nums if x != '']

        print(card)
        print(winning_nums, my_nums)

        pts = 0
        for n in my_nums:
            if n in winning_nums:
                if pts == 0:
                    pts += 1
                else:
                    pts *= 2
        ans += pts
        print(cardNum, pts)
        cardNum += 1

    print(ans)
solve()