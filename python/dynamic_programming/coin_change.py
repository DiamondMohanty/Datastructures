# Coin Change Problem: Implementation of classical dynamic programming problem
# Given some coins determine if you can return the target change to the customer. 
# A coin can be used only once
# Author: Diamond Mohanty
# Date: 20-Jan-2022

from typing import List


def coin_change(target: int, coins: List[int]):
    if target == 0:
        return True
    elif target < 0:
        return False
    for coin in coins:
        new_target = target - coin
        coins.remove(coin) 
        res = False or coin_change(new_target, coins)
        if res == True:
            return True
    return False
        

# Driver Code
target = 14
coins = [4,2, 2, 6]
print(coin_change(target, coins))
