total = 0
piece1 = 0
piece2 = 0
def rod_cutting(prices, length, start):
    global total, piece1, piece2
    if length == 1:
        return prices[0]
    if start == 0:
        if prices[length-1] > total:
            total = prices[length-1]
            piece1 = start
            piece2 = length
    elif prices[length-1] + prices[start-1] > total:
        total = prices[length-1] + prices[start-1]
        piece1 = start
        piece2 = length
    rod_cutting(prices, length - 1, start + 1) + prices[length-1]
    return total
print(rod_cutting([1,5,8,3,10,17], 4, 0))
print("Pieces " +  str(piece1) + " and " + str(piece2))