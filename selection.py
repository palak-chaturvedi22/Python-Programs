# import unittest

def selectionSort(arr):
    n = len(arr)

    for i in range(0,n-1):
        min_ele = i

        for j in range(i+1,n):
            if arr[j] < arr[min_ele]:
                min_ele = j
        
        temp = arr[min_ele]
        arr[min_ele] = arr[i]
        arr[i] = temp


# class selectionSort_tests(unittest.TestCase):
#     def sort(self,arr):
#         a = arr[:]
#         selectionSort(a)
#         return a
    
#     def test_even_case(self):
#         arr = [4,2,8,5]
#         arr1 = self.sort(arr)
#         self.assertEqual(arr1, [2,4,5,8])
 
#     def test_odd_case(self):
#         arr = [4,8,5]
#         arr1 = self.sort(arr)
#         self.assertEqual(arr1, [4,5,8])

# class Hello_tests(unittest.TestCase):
#     def sort(self,arr):
#         a = arr[:]
#         selectionSort(a)
#         return a
#     def test_duplicate(self):
#         arr = [2,2,3,1]
#         arr1 = self.sort(arr)
#         self.assertEqual(arr1, [1,2,2,3])

# if __name__ == "__main__":
#     unittest.main()
n=int(input("Number of elements in the array:-"))
arr =list(map(int, input("elements of array:-").strip().split()))

selectionSort(arr)

for i in range(n):
    print(arr[i])
