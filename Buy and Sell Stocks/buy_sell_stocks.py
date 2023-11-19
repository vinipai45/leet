def get_max(a:int,b:int):
    if(a>b):
        return a
    return b

def get_profit(arr:list[int]):

    buy=0
    sell=1
    profit = -1

    while sell < len(arr):
        
        if( arr[buy] >= arr[sell] ):
            buy = sell
            sell = sell + 1

        else :
            profit = get_max(profit, arr[sell] - arr[buy])
            sell = sell + 1

    if profit > 0 :  
        return profit
    
    return 0


def main():

    prices = list(map(int, input().split())) #[7,1,5,3,6,4]

    result = get_profit(prices)

    print(result)

main()