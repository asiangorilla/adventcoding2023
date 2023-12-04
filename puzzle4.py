def list_of_string_to_int(written_list: str):
    int_list = []
    curr_numb = ''
    looking_at_numb = False
    for i in range(len(written_list)):
        if not written_list[i].__eq__(' '):
            looking_at_numb = True
            curr_numb += written_list[i]
        if (looking_at_numb and written_list[i].__eq__(' ')) or i == len(written_list) - 1:
            int_list.append(int(curr_numb))
            curr_numb = ''
            looking_at_numb = False
    return int_list


with open('input/input4.txt') as f:
    lines = f.readlines()
total = 0
copies = [1]*len(lines)
# processing input
for i, line in enumerate(lines):
    col_pos = line.find(':')
    numbers = line[col_pos + 1:]
    pipe_pos = numbers.find('|')
    winning_numbs_str = numbers[:pipe_pos].strip()
    card_numbs_str = numbers[pipe_pos + 1:].strip()

    winning_numbs = list_of_string_to_int(winning_numbs_str)
    card_numbs = list_of_string_to_int(card_numbs_str)

    # check card value
    hits = 0
    for numbs in card_numbs:
        for win_numb in winning_numbs:
            if numbs == win_numb:
                hits += 1

    if hits == 0:
        val = 0
    else:
        val = pow(2, hits - 1)
        for j in range(hits):
            copies[i+j+1] += copies[i]

    total += val
print(total)
print(sum(copies))
