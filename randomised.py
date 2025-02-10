import random

def randomized_quick_sort(arr, low, high):
    if low < high:
        # Pick a random pivot and swap with the last element
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Partition the array around the random pivot
        pivot = partition(arr, low, high)
        
        # Recursively sort the partitions
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pivot is now at the end
    i = low - 1  # Pointer for smaller elements
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements to maintain order

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1

# Example Usage
arr = [10, 7, 8, 9, 1, 5]
randomized_quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
