# import unittest

def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


#Test cases from here 
# class bubble_tests(unittest.TestCase):
#     def sort(self, arr):
#         copy = arr[:]
#         bubble(copy)
#         return copy

#     def test_odd_number(self):
#         #Arrange
#         arr= [3,2,7,4,2]
#         #Act
#         arr1= self.sort(arr)
#         #assert
#         self.assertEqual(arr1, [2,2,3,4,7])

#     def test_even_number(self):
#         arr=[8,2,9]

#         arr1=self.sort(arr)
#         self.assertEqual(arr1, [2,8,9])
    
#     def test_duplicate_number(self):
#         arr = [8,9,9,2]

#         arr1= self.sort(arr)

#         self.assertEqual(arr1, [2,8,9,9])
        

# if __name__ == "__main__":
#     unittest.main()
n = int(input("Number of elements in the array:-"))
arr = list(map(int, input("elements of array:-").strip().split()))
bubble(arr)


for i in range(n):
    print(arr[i])
