#task 11 linear seaerch

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Example usage
numbers = [10, 23, 45, 70, 11, 15]
target = int(input("ENter the element to be searched"))
result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")