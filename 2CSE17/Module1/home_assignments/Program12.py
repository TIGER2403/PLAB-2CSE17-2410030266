def get_min_diff(arr, k):
    n = len(arr)
    arr.sort()
    ans = arr[-1] - arr[0]   
    for i in range(1, n):
        if arr[i] - k < 0:
            continue       
        minimum = min(arr[0] + k, arr[i] - k)
        maximum = max(arr[i - 1] + k, arr[-1] - k)      
        ans = min(ans, maximum - minimum)   
    return ans
arr1 = [1, 5, 8, 10]
k1 = 2
print(get_min_diff(arr1, k1))
arr2 = [3, 9, 12, 16, 20]
k2 = 3
print(get_min_diff(arr2, k2))
