
Nums = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']

with open('input/input.txt') as f:
    lines = f.readlines()

def stringToNum(b:str):
    for i in range(9):
        if b.__eq__(Nums[i+9]):
            return str(i+1)


def checkIfStringNum(a:str):
    firstPos = -1
    secondPos = -1
    first = ''
    second = ''
    for num in Nums:
        pos = a.find(num)
        rpos = a.rfind(num)
        if pos >= 0:
            if firstPos == -1 or pos < firstPos:
                if not firstPos == -1 and secondPos == -1:
                    secondPos = firstPos
                    second = first
                firstPos = pos
                if len(num)>1:
                    first = stringToNum(num)
                else:
                    first = num
            elif secondPos == -1 or pos > secondPos:
                secondPos = pos
                if len(num)>1:
                    second = stringToNum(num)
                else:
                    second = num
            if (not pos == rpos) and rpos > secondPos:
                secondPos = rpos
                if len(num)>1:
                    second = stringToNum(num)
                else:
                    second = num
    return (first, second)


total = 0

for line in lines:
    first, second = checkIfStringNum(line)
    if not second:
        num = int(first+first)
    else:
        num = int(first+second)
    total += num

print(total)