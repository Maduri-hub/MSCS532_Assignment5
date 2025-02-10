def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a single-element or empty array is already sorted
    
    pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    
    return quicksort(left) + middle + quicksort(right)  # Recursively sorting and combining

# Example usage
data = [3, 6, 8, 10, 1, 2, 1]
sorted_data = quicksort(data)
print(sorted_data)