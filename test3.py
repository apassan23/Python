def lottery(x):
    hash_x = int(x*7/2 % 10)

    def yourPrize(x):
        if x >= 15:
            prize = "prize money: $10k"
        if x >= 10:
            prize = "prize money: $5k"
        if x >= 5:
            prize = "prize money: $1k"
        if x >= 1:
            prize = "Prize Money: $50"
        else:
            prize = "sorry"
        return prize
    return yourPrize(hash_x)


for i in range(1, 6):
    print(lottery(i))
