# Sorting a positional List
# Author: Diamond Mohanty
# Date: 29 Jan 2022


from sympy import li
from postionallist import PostionList

list = PostionList()
list.add_last(15)
list.add_last(23)
list.add_last(25)
list.add_last(7)
list.add_last(19)
list.add_last(10)

for pos in list:
    print(pos, end=' ')

def insertion_sort(list: PostionList):
    cursor = list.first()
    while cursor:
        local = list.after(cursor)
        for pos in list:
            print(pos, end=' ')
        while local:
            if local.element() <= cursor.element():
                list.add_before(local.element(), cursor)
                temp = local
                local = list.after(local)
                list.delete(temp)
                continue
                
            local = list.after(local)
        cursor = list.after(cursor)
    return list
print()
list = insertion_sort(list)
print('== After Sorting ==')
for pos in list:
    print(pos, end=' ')


        
