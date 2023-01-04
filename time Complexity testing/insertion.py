# import unittest

# time complexity of random function is O(1)
import random as r
def insertionA(arr):
    s= len(arr)
    # one loop = n
    for i in range(1, s):  
        temp = arr[i]
        j=i-1
        
        while (j >= 0 and temp < arr[j]):
            arr[j+1] = arr[j]
            j= j-1
        
        arr[j+1] = temp


# test case starts from here
# class insertion_tests(unittest.TestCase):
#     def sort(self,arr):
#         copy = arr[:]
#         insertionA(copy)
#         return copy
    
#     def test_even_number(self):
#         arr = [9,4,6,5]
#         arr1 = self.sort(arr)

#         self.assertEqual(arr1, [4,5,6,9])

#     def test_duplicate_numbers(self):
#         arr = [4,7,3,2,2]
#         arr1 = self.sort(arr)

#         self.assertEqual(arr1, [2,2,3,4,7])
# if __name__ == "__main__":
#     unittest.main()

# arr =input("elements of array:-").split()
# arr = [int(x) for x in arr]
arr=[]
for _ in range(0,100):
    r1 = r.randint(0,100)
    arr.append(r1)
# print(arr)
print(arr)
insertionA(arr)
print("Sorted list : ")
print(arr)

