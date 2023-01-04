def findResult(x,arr):
    n=len(arr)
    for i in range(0,n):
        if arr[i] == x:
            return i
    
if __name__ == "__main__":
    x = int(input("Enter the digit to be found: "))
    arr=list(map(int, input("Enter the elements of the array: ").strip().split()))
    result = findResult(x,arr)
    if result == x:
        print("The number has been found")

    else:
        print("Number is not found")


