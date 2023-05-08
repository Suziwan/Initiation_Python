# coder un programme qui permet, à partir d'une liste de prix, de connaître le meilleur jour d'achat 
# et le meilleur jour de revente pour faire le maximum de bénéfices.

def day_trader(list_prices):
    max_price = 0
    for buy_day in range(0, len(list_prices)):
        for sell_day in range(buy_day+1, len(list_prices)):
            price = list_prices[sell_day] - list_prices[buy_day]
            if price > max_price:
                max_price = price
                best_buy_day = buy_day
                best_sell_day = sell_day
    print('The best day to buy is day ' + str(best_buy_day) + ', to sell on day ' + str(best_sell_day) + 
          ' for a total price of $' + str(max_price) +'.')
        
day_trader([17, 3, 6, 9, 15, 8, 6, 1, 10])