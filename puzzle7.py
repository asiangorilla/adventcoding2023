# processing input

'''
#part1
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
'''
# part2

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def find_in_order(c: str):
    for i in range(len(order)):
        if c.__eq__(order[i]):
            return i
    return -1


def amount_in_str(char: str, x: str):
    amount = 0
    for char_x in x:
        if char.__eq__(char_x):
            amount += 1
    return amount


def compare_same(x: str, y: str):
    for j in range(len(x)):
        if find_in_order(x[j]) < find_in_order(y[j]):
            return 0  # x hand is higher rank
        elif find_in_order(x[j]) > find_in_order(y[j]):
            return 1  # y hand is higher rank
    return -1


'''
#part1
def hand_val(x: str):
    # x_hand denotes hand value from 6 (five of a kind) to 0 (high card)
    x_hand = 0
    for char in order:
        if x_hand >= 4:
            break  # if hand is full_house, or above, you cannot get any better
        am = amount_in_str(char, x)
        if am >= 4:
            x_hand = am + 1
        elif am == 3:  # either x_hand had one pair or nothing, which means you move up 3 regardless
            x_hand += 3
        elif am == 2:  # if you find a pair, no matter what you were before, you move up in the ranking
            x_hand += 1
    return x_hand
'''


# part2
def hand_val(x: str):
    # x_hand denotes hand value from 6 (five of a kind) to 0 (high card)
    x_hand = 0
    am_j = amount_in_str('J', x)
    if am_j >= 4:
        return 6
    if am_j == 3:
        for ord_in_val_func in order[:-1]:
            am = amount_in_str(ord_in_val_func, x)
            if am > 0:
                return 4 + am
    if am_j == 2:
        for ord_in_val_func in order[:-1]:
            am = amount_in_str(ord_in_val_func, x)
            if am == 3:  # five of a kind possible
                return 6
            if am == 2:  # 2 of a kind possible
                return 5
        return 3  # only three of a kind possible
    if am_j == 1:
        might_be_full_house = False
        for ord_in_val_func in order[:-1]:
            am = amount_in_str(ord_in_val_func, x)
            if am == 4:
                return 6
            elif am == 3:
                return 5
            elif am == 2:
                if might_be_full_house:
                    return 4
                else:
                    might_be_full_house = True
        if might_be_full_house:
            return 3
        else:
            return 1
    if am_j == 0:
        for char in order[:-1]:
            if x_hand >= 4:
                break  # if hand is full_house, or above, you cannot get any better
            am = amount_in_str(char, x)
            if am >= 4:
                x_hand = am + 1
            elif am == 3:  # either x_hand had one pair or nothing, which means you move up 3 regardless
                x_hand += 3
            elif am == 2:  # if you find a pair, no matter what you were before, you move up in the ranking
                x_hand += 1
    return x_hand


def quicksort_hands(hand_arr: [(str, str, int)], type: int):
    if len(hand_arr) <= 1:
        return hand_arr
    pivot = hand_arr[len(hand_arr) // 2]
    if type == 0:
        left = [x for x in hand_arr if x[2] < pivot[2]]
        middle = [x for x in hand_arr if x[2] == pivot[2]]
        if len(middle) > 1:
            middle = quicksort_hands(middle, 1)
        right = [x for x in hand_arr if x[2] > pivot[2]]
    else:
        left = [x for x in hand_arr if compare_same(x[0], pivot[0]) == 1]
        middle = [x for x in hand_arr if compare_same(x[0], pivot[0]) == -1]  # middle should always only have size 1
        right = [x for x in hand_arr if compare_same(x[0], pivot[0]) == 0]
    return quicksort_hands(left, type) + middle + quicksort_hands(right, type)


with open('input/input7.txt') as f:
    lines = f.readlines()

hands = []

for line in lines:
    parts = line.replace('\n', '').split(' ')
    hands.append((parts[0], parts[1], hand_val(parts[0])))
# calculation

hands = quicksort_hands(hands, 0)

total = 0
for i, hand in enumerate(hands):
    total += (i + 1) * int(hand[1])
