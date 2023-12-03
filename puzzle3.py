

def printSurroundings(lines, i, j):
    for l in range(10):
        l_prime = l - 5
        output = ''
        for m in range(10):
            m_prime = m-5
            if i + l_prime >= len(lines) or i + l_prime < 0:
                continue
            elif j + m_prime >= len(lines[i + l_prime]) or j + m_prime < 0:
                continue
            else:
                output += lines[i+l_prime][j+m_prime] + ' '
        output += '\n'
        print(output)


#for every digit found, find the number and change it to dots in lines. Return the number
def findNumber(lines:[str], i:int, j:int):
    number_not_found_l = True
    number_not_found_r = True
    l = j
    r = j
    while number_not_found_l or number_not_found_r:
        if number_not_found_r:
            if r == len(lines[i]) or not lines[i][r].isnumeric():
                number_not_found_r = False
            else:
                r += 1
        if number_not_found_l:
            if not lines[i][l].isnumeric() or l == 0:
                number_not_found_l = False
                if not lines[i][l].isnumeric():
                    l += 1
            else:
                l -= 1
    h1 = lines[i][l:r]
    num = int(h1)
    h2 = ''
    for o in range(len(h1)):
        h2 += '.'
    lines[i] = lines[i][:l] + h2 + lines[i][r:]
    return num


with open('input/input3.txt') as f:
    lines = f.readlines()

total = 0
total_ratio = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    for j in range(len(lines[i])):
        if not (lines[i][j].isnumeric() or lines[i][j].__eq__('.')):
            #printSurroundings(lines, i, j)
            #print(lines[i][j])
            #we are looking at a symbol
            #check every adjecent block for number
            isGear = False
            adj = 0
            hList = []
            if lines[i][j].__eq__('*'):
                isGear = True
            for l in range(3):
                lPrime = l-1
                for m in range(3):
                    mPrime = m-1
                    if i+lPrime >= len(lines) or i+lPrime < 0:
                        continue
                    elif j+mPrime >= len(lines[i+lPrime]) or j+mPrime < 0:
                        continue
                    elif lines[i+lPrime][j+mPrime].isnumeric():
                        h = findNumber(lines, i+lPrime, j+mPrime)
                        adj += 1
                        total += h
                        hList.append(h)
                        #print(h)
            if isGear and adj == 2:
                total_ratio += hList[0]*hList[1]
            #printSurroundings(lines, i, j)
with open('input/output3.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')
    f.close()
print(total)
print(total_ratio)

