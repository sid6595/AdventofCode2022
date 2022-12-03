import math

results, badges = [], []
firsthalf, secondhalf = [], []

def char_score(letter):
    if letter.isupper() == True:
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def make_compartments(line):
    for i in range(math.floor(len(line) / 2)):
        firsthalf.append(line[i])
    for j in range(math.floor(len(line)/2), len(line)) :
        secondhalf.append(line[j])
    return firsthalf, secondhalf
         
with open("input.txt") as f:
    current, line1, line2, line3 = 1, [], [], []
    for line in f:
        #part 1
        make_compartments(line)
        results.append(char_score(list(set(firsthalf).intersection(secondhalf))[0]))
        firsthalf, secondhalf = [], []

        #part 2
        listofchars=[i for i in line.strip()]
        if current % 3 == 1:
            line1 = listofchars
        if current % 3 == 2:
            line2 = listofchars
        if current % 3 == 0:
            line3 = listofchars
            badges.append(char_score(list(set(line1).intersection(line2, line3))[0]))
        current += 1

print("Part 1: ", sum(results))
print("Part 2: ", sum(badges))

    

