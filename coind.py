coins = [1]
amount = 0

def combinations(coins,amount):
    result=[]
    def valuefetcher(temp,coins,amount):
        for i in coins:
            if i>amount:
                break
            temp.append(i)
            if i==amount:
                result.append(temp.copy())
                temp.pop()
                break
            else:
                idx=coins.index(i)
                valuefetcher(temp,coins[idx:],amount-i)
                temp.pop()

    valuefetcher([], coins, amount)


    return len(sorted(result,key=lambda x:len(x))[0])


print(combinations(coins,amount))