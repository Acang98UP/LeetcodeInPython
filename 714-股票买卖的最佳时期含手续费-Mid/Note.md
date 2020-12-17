### 利用动态规划解决股票问题
___
+ 解题思路  
维护一组买入和卖出价格buy和sell，然后遍历数组  
> 当buy<sell-fee时代表一组能够盈利的备用投资方案，若在此时：  
> + prices[i]<sell-fee，说明这次卖出后依然可以找到一个让收益更大的买入价格。  
> + 将sell-buy-fee写入总收益，并更新sell=buy=prices[i]
> + 当prices[i]>sell时，更新sell=prices[i]，可以使当前投资方案收益更高  

> 当 buy>=sell-fee 时，说明此时无备用投资方案，此时若：
> + prices[i]>sell 更新sell=prices[i]  
> + prices[i]<buy 更新sell=buy=prices[i]
  
```
def maxProfit(prices: List[int], fee: int) -> int:
    sell = buy = prices[0]
    profit = 0
    for x in prices:
        if buy < sell - fee:
            if x < sell - fee:
                profit += (sell - buy - fee)
                sell = buy = x
            elif x > sell:
                sell = x
        else:
            if x > sell:
                sell = x
            if x < buy:
                sell = buy = x
    if buy < sell - fee:
        profit += (sell - buy - fee)
    return profit
```

___
### 利用贪心算法进行解答
___
