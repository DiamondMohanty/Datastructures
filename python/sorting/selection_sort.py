# Selection sort implementation
# Author: Diamond Mohanty
# Date: 19-Jan-2022

from typing import List
import math

def selection_sort(nums: List[int]) -> List[int]:
    for idx in range(len(nums)):
        low = math.inf
        pos = -1
        for jidx in range(idx + 1, len(nums)):
            if nums[jidx] < low:
                low = nums[jidx]
                pos = jidx
        if pos != -1 and low < nums[idx]:
            temp = nums[idx]
            nums[idx] = nums[pos]
            nums[pos] = temp

    return nums

# Driver Code
arr = [1,5,2,9,3,6,7]
print(selection_sort(arr))

