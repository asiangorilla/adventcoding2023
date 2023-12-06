import re

# processing input
with open('input/input6.txt') as f:
    lines = f.readlines()

times = lines[0][lines[0].find(':') + 1:].strip()
distances = lines[1][lines[1].find(':') + 1:].strip()

times = re.split('\\s+', times)
distances = re.split('\\s+', distances)

''' 
#part 1
times = [int(num) for num in times]
distances = [int(num) for num in distances]
'''
# part2
times = int(''.join(times))
distances = int(''.join(distances))

# calculations
'''
#part1
amount_win_mult = 1


for i, time in enumerate(times):
    distance = distances[i]
    beat_amount = 0
    for j in range(time):
        my_distance = j * (time - j)
        if my_distance > distance:
            beat_amount += 1
    amount_win_mult *= beat_amount

print(amount_win_mult)
'''

# part2
beat_amount = 0
for j in range(times):
    my_distance = j * (times - j)
    if my_distance > distances:
        beat_amount += 1
print(beat_amount)
