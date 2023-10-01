def heapify(arr, n, i):
    smallest = i  # Initialize the root as the smallest element
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if the left child exists and is smaller than the root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Check if the right child exists and is smaller than the current smallest
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest element is not the root, swap them
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum) element with the last element
        heapify(arr, i, 0)  # Call heapify on the reduced heap
    arr1 = list(reversed(arr))
    return arr1

import heapq

def heapSort(arr):
    heapq.heapify(arr)
    result = []

    while arr:
        result.append(heapq.heappop(arr))
    return result


input_array = [4, 10, 3, 5, 1]
sorted_array = heap_sort(input_array)
print(sorted_array) 
