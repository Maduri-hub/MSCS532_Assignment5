import random
import time

# Deterministic Quicksort (Pivot: Last Element)
def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        deterministic_quick_sort(arr, low, pivot - 1)
        deterministic_quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized Quicksort
def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap random pivot with last element
        pivot = partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)

# Function to run and time sorting
def time_sorting(algorithm, arr):
    start = time.time()
    algorithm(arr, 0, len(arr) - 1)
    end = time.time()
    return end - start

# Generate test data
def generate_test_data(size, order="random"):
    arr = list(range(size))
    if order == "random":
        random.shuffle(arr)
    elif order == "reverse":
        arr.reverse()
    return arr

# Run experiments
sizes = [100, 500, 900]
orders = ["random", "sorted", "reverse"]

for size in sizes:
    print(f"\n--- Input Size: {size} ---")
    for order in orders:
        arr1 = generate_test_data(size, order)
        arr2 = list(arr1)  # Copy to ensure same input for both algorithms

        time_det = time_sorting(deterministic_quick_sort, arr1)
        time_rand = time_sorting(randomized_quick_sort, arr2)

        print(f"  {order.capitalize()} input: Deterministic = {time_det:.6f} sec, Randomized = {time_rand:.6f} sec")
