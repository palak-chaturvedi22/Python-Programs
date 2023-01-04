# import unittest


import random as r

def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


# class quick_tests(unittest.TestCase):
#     def sort(self, alist):
#         a = alist[:]
#         quicksort(a, 0, len(a))
#         return a

#     def test_func(self):
#         alist = [5, 6, 7, 9, 8, 1, 33]
#         arr = self.sort(alist)
#         self.assertEqual(arr, [1, 5, 6, 7, 8, 9, 33])


# if __name__ == '__main__':
#     unittest.main()
# alist = input('Enter the list of numbers: ').split()
# alist = [int(x) for x in alist]
alist=[]
for _ in range(0,100):
    r1=r.randint(0,100)
    alist.append(r1)
print(alist)
quicksort(alist, 0, len(alist))
print('Sorted list: ')
print(alist)
