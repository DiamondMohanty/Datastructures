# Predict the output of each code snippet
# Author: Diamond Mohanty
# Date: 04-Jan-2022

# 1
from typing import List


ndarray = [[0] * 3] * 3
ndarray[0][1] = 100
print(ndarray[1][1], ndarray[2][0])

#2
ndarray = [[0] * 3 for _ in range(3)]
ndarray[0][1] = 100
print(ndarray[1][1], ndarray[2][0])

#3
class Student():
    def __init__(self) -> None:
        self._id = 1

    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        self._id = id


s1 = Student()
s2 = Student()
s3 = Student()

arr: List[Student] = [s1, s2, s3]
slice = arr[2:]
slice[0].set_id(100)

print(arr[2].get_id(), slice[0].get_id())

#4
arr = [0] * 3
slice = arr[2:]
slice[0] = 100

print(arr[2], slice[0])