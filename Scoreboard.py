players = [
    ["Name","Kills","Deaths"],
    ["k1llmAchine",51,49],
    ["bob2247",5,99],
    ["hAxOr12",72,30]
]
print("-"*26)
for player in players:
    print("|{0:<11}|{1:<5}|{2:<6}|".format(player[0],player[1],player[2]))
    print("-"*26)
