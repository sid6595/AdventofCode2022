
def make_list(filename):
    list = []
    sum = 0

    with open(filename, 'r') as f:
        #return f.read()
        for line in f:
            data = line.split()
            if line.strip():
                var = (int(data[0]))
                sum += var
            else:
                list.append(sum)
                sum = 0

        #for x in range(len(list)):
            #print(list[x])
        return list       


def greatest(list):
    greatest = 0
    for i in list:
        if i > greatest:
            greatest = i
            #print(greatest)
    return greatest

def top3(list):
    top = []

    for i in range(3):
        top.append(max(list))
        list.remove(max(list))

    return sum(top)

newlist = make_list('1.1input.txt')
print(top3(newlist))



