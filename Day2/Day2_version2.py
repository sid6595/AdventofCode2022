results, results2, dictionary, possible = [], [], {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}, [1, 2, 3]

def line_result(opponent, user, optimal):
    opp_val, user_val= dictionary.get(opponent), dictionary.get(user)
    if optimal == False:
        if opp_val == user_val:
            return user_val + 3
        if user_val == opp_val + 1 or user_val == opp_val - 2:
            return user_val + 6
        else:
            return user_val
    else:
        if user == "Y":
            return opp_val + 3
        if user == "Z":
            return possible[(possible.index(opp_val) + 1) % len(possible)] + 6
        if user == "X":
            return possible[(possible.index(opp_val) - 1) % len(possible)]

with open("input.txt", 'r') as f:
    for line in f:
        results.append(line_result(line[0], line[2], False))
        results2.append(line_result(line[0], line[2], True))

print("The strategy 1 score is: ", sum(results))
print("The optimal strategy score is:", sum(results2))