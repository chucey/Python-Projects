from Crytpo_data import get_coin, Coin

def alert(symbol:str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol ==symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!TRIGGERED!!')
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coin()

    alert('btc', bottom=20000, top=30000, coins_list=coins)