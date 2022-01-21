# Merge sort implementation
# Author: Diamond Mohanty
# Date: 19-Jan-2022

from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) == 1: # Stopping condition
        return nums
    elif len(nums) == 2: # Stopping condition
        if nums[0] < nums[1]:
            return nums
        else:
            return [nums[1], nums[0]]
    
    mid = len(nums) // 2
    
    left = merge_sort(nums[0: mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(nums1: List[int], nums2: List[int]) -> List[int]:
    merged_nums = []
    idx = 0
    jidx = 0
    while idx < len(nums1):
        if jidx == len(nums2) - 1: # Scanning of one array finished
            break

        if nums2[jidx] < nums1[idx]:
            merged_nums.append(nums2[jidx])
            jidx += 1
        else:
            merged_nums.append(nums1[idx])
            idx += 1

    # Leftovers
    while idx < len(nums1):
        merged_nums.append(nums1[idx])
        idx += 1

    while jidx < len(nums2):
        merged_nums.append(nums2[jidx])
        jidx += 1
    
    return merged_nums
# Driver Code
arr = [1,5,2,9,3,6,7]
print(merge_sort(arr))
