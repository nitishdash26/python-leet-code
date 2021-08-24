def best_time_sell_stock(prices):
    sell = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        buy = min(buy, prices[i])
        sell = max(sell, prices[i] - buy)
    return sell


print(best_time_sell_stock([7,1,5,3,6,4]))
