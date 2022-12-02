list,sums = [],0

with open("input.txt", 'r') as f:
    for line in f:
        if line.strip():
            sums += int(line)
        else:
            list.append(sums)
            sums = 0
            
list.sort()

print("The greatest sum is: ", list[-1])
print("The top 3 sums are: ", sum(list[-3:]))

