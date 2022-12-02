"""
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Part 1
X - Rock
Y - Paper
Z - Scissors
"""

"""
Part 2
The second column says how the round needs to end:
X means you need to lose
Y means you need to end the round in a draw
Z means you need to win
"""

results = []
results2 = []
dictionary = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

new_dict = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : "lose",
    "Y" : "draw",
    "Z" : "win"
}

def line_result(opponent, user):
    opp_val = dictionary.get(opponent)
    user_val = dictionary.get(user)
    
    #draw
    if opp_val == user_val:
        return user_val + 3
    #win
    if user_val == opp_val + 1:
        return user_val + 6
    #win
    if user_val == opp_val - 2:
        return user_val + 6
    #lose
    else:
        return user_val

def line_result2(opponent, user):
    opp_val = new_dict.get(opponent)
    user_val = new_dict.get(user)
    
    #draw
    if user_val == "draw":
        return opp_val + 3
    #win
    if user_val == "win" and opp_val == 3:
        return 7
    #win
    if user_val == "win":
        return opp_val + 7
    #lose
    if user_val == "lose" and opp_val == 1:
        return 3
    #lose
    else:
        return opp_val - 1

with open("input.txt", 'r') as f:
    for line in f:
        results.append(line_result(line[0], line[2]))
        results2.append(line_result2(line[0], line[2]))

print("The strategy 1 score is: ", sum(results))
print("The optimal strategy score is:", sum(results2))

            
