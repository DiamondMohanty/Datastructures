# Insertion sort implementation
# Author: Diamond Mohanty
# Date: 19-Jan-2022

from typing import List
def insertion_sort(nums: List[int]) -> List[int]:
    for idx in range(len(nums)):
        for jidx in range(idx + 1, len(nums)):
            if nums[jidx] < nums[idx]:
                temp = nums[jidx]
                # Right Shift the elements
                walk = jidx
                while walk > idx:
                    nums[walk] = nums[walk - 1]
                    walk -= 1
                nums[idx] = temp
    return nums

# Driver Code
arr = [1,5,2,9,3,6,7]
print(insertion_sort(arr))

