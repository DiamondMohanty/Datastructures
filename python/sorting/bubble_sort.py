# Bubble sort implementation
# Author: Diamond Mohanty
# Date: 19-Jan-2022

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    idx = 0
    for idx in range(len(nums)):
        for jidx in range(idx + 1, len(nums)):
            if nums[idx] > nums[jidx]:
                temp = nums[jidx]
                nums[jidx] = nums[idx]
                nums[idx] = temp
    return nums

# Driver Code
arr = [1,5,2,9,3,6,7]
print(bubble_sort(arr))