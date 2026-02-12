def max_subarray_sum(arr):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global


# Example
arr = [2, 3, -8, 7, -1, 2, 3]
print(max_subarray_sum(arr))
