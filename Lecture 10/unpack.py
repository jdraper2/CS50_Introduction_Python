def total(galleons, sickels, knuts):
    return (galleons * 17 + sickels) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "knuts")

coins2 = {"galleons": 100, "sickels": 50, "knuts": 25}

print(total(coins2["galleons"], coins2["sickels"], coins2["knuts"]), "Knuts")
print(total(**coins2), "Knuts")