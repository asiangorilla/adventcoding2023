# process input


with open('input/input5.txt') as f:
    lines = f.readlines()

# first line is seeds
col_pos = lines[0].find(':')
seeds_str = lines[0][col_pos + 2:-1]

seeds_str = seeds_str.split(' ')
seeds = []
for seed_str in seeds_str:
    seeds.append(int(seed_str))

maps = []
map_idx = -1
curr_map = []
for i in range(2, len(lines)):
    if not lines[i].find(':') == -1:
        if not map_idx == -1:
            maps.append(curr_map)
            curr_map = []
        map_idx += 1
    elif lines[i].__eq__('\n'):
        continue
    else:
        nums_str = lines[i].replace('\n', '').split(' ')
        nums = []
        for num_str in nums_str:
            nums.append(int(num_str))
        curr_map.append(nums)
    if i == len(lines) - 1:
        maps.append(curr_map)

# calculation
'''
#part1 with a part 2 brute force
minimum = 0
for i in range(0, len(seeds), 2):
    for j in range(seeds[i + 1]):
        curr_mapped_num = seeds[i] + j
        for mapping in maps:
            for unmapping in mapping:
                if unmapping[1] <= curr_mapped_num <= unmapping[1] + unmapping[2]:
                    curr_mapped_num += unmapping[0] - unmapping[1]
                    break  # if we found a submapping that fits, we don't need to find another fitting submapping
        if minimum == 0 or minimum > curr_mapped_num:
            minimum = curr_mapped_num
'''

# part2
minimum = -1
for i in range(0, len(seeds), 2):
    seed_ranges = [[seeds[i], seeds[i]+seeds[i + 1]-1]]
    for mapping in maps:
        new_seed_ranges = []
        for sub_mapping in mapping:
            for seed_range in seed_ranges:
                if sub_mapping[1] < seed_range[0] <= sub_mapping[1] + sub_mapping[2] < seed_range[1]:
                    new_seed_ranges.append(
                        [seed_range[0] + sub_mapping[0] - sub_mapping[1], sub_mapping[0] + sub_mapping[2]])
                    new_seed_ranges.append([sub_mapping[1] + sub_mapping[2] + 1, seed_range[1]])
                elif seed_range[0] < sub_mapping[1] and sub_mapping[1] + sub_mapping[2] < seed_range[1]:
                    new_seed_ranges.append([seed_range[0], sub_mapping[1] - 1])
                    new_seed_ranges.append([sub_mapping[0], sub_mapping[0] + sub_mapping[2]])
                    new_seed_ranges.append([sub_mapping[1] + sub_mapping[2] + 1, seed_range[1]])
                elif seed_range[0] < sub_mapping[1] <= seed_range[1] < sub_mapping[1] + sub_mapping[2]:
                    new_seed_ranges.append([seed_range[0], sub_mapping[1] - 1])
                    new_seed_ranges.append([sub_mapping[0], seed_range[1] + sub_mapping[0] - sub_mapping[1]])
                elif sub_mapping[1] <= seed_range[0] and seed_range[1] <= sub_mapping[1] + sub_mapping[2]:  # map whole
                    # seed range
                    new_seed_ranges.append(
                        [seed_range[0] + sub_mapping[0] - sub_mapping[1], seed_range[1] + sub_mapping[0]
                         - sub_mapping[1]])
        if not len(new_seed_ranges) == 0:
            seed_ranges = new_seed_ranges.copy()
    if minimum == -1:
        minimum = seed_ranges[0][0]
    for seed_range in seed_ranges:
        if minimum > seed_range[0]:
            minimum = seed_range[0]

print(minimum)
