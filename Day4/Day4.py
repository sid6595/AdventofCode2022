import re
containedpairs, touchingpairs = 0, 0
def makelists(line):
    ints = [int(s) for s in re.split(r',|-', line.strip()) if s.isdigit()]
    #print(ints)
    for i in range(ints[0], ints[1] + 1):
        set1.append(i)
    for j in range(ints[2], ints[3] + 1):
        set2.append(j)
    #print(set1), print(set2)

def ispair(one, two):
    return all(items in one for items in two) or all(items in two for items in one)

def istouching(one, two):
    return any(items in one for items in two) or any(items in two for items in one)

#text = "2-4,6-8  "
#makelists(text)

test1 = [6]
test2 = [4,5,6]
with open("input.txt", 'r') as f:
    for line in f:
        set1, set2 = [], []
        makelists(line)
        if ispair(set1, set2):
            containedpairs += 1
        if istouching(set1, set2):
            touchingpairs += 1
            
print("Overlapping: ", containedpairs)
print("Touching: ", touchingpairs)
