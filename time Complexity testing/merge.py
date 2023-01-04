# import unittest

import random as r

def merge_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
 
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

# class mergeSort_tests(unittest.TestCase):
#     def sort(self, alist):
#         a= alist[:]
#         b= merge_sort(a,0,len(alist))
#         # merge_list(b,0,len(alist))
#         return a
    
#     def test_func(self):
#         arr = [4,5,7,1,6,8]
#         arr1 = self.sort(arr)
#         self.assertEqual(arr1, [1, 4, 5, 6, 7, 8])

        



# if __name__ == "__main__":  
#     unittest.main()  
# alist = input('Enter the list of numbers: ').split()
# alist = [int(x) for x in alist]
alist=[]
for _ in range(0,100):
    r1= r.randint(0,99)
    alist.append(r1)
print(alist)
merge_sort(alist, 0, len(alist))
print('Sorted list: ')
print(alist)