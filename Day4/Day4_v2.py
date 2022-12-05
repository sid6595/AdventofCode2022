import re
containedpairs, touchingpairs = 0, 0
with open("input.txt", 'r') as f:
    for line in f:
        set1, set2, ints = [], [], [int(s) for s in re.split(r',|-', line.strip()) if s.isdigit()]
        for i in range(ints[0], ints[1] + 1):
            set1.append(i)
        for j in range(ints[2], ints[3] + 1):
            set2.append(j)
        if all(items in set1 for items in set2) or all(items in set2 for items in set1):
            containedpairs += 1
        if any(items in set1 for items in set2) or any(items in set2 for items in set1):
            touchingpairs += 1
print("Overlapping: ", containedpairs)
print("Touching: ", touchingpairs)
