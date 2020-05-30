import json

with open("players.json") as json_file:
    players = json.load(json_file)["players"]

    net = 0.0
    for i in range(len(players)):
        net += players[i]["earnings"]

    if round(net, 2) != 0.0:
        raise Exception('Imbalance detected. Total gains do not equal total losses.')

    for i in range(len(players)):
        j = 0
        while round(players[i]["earnings"], 2) < 0.0:
            if j != i and players[j]["earnings"] > 0.0:
                amount = round(min(abs(players[i]["earnings"]), players[j]["earnings"]), 2)
                players[i]["earnings"] += amount
                players[j]["earnings"] -= amount
                print("{} sends {} ${:,.2f}".format(players[i]["name"], players[j]["name"], amount))
            j += 1
