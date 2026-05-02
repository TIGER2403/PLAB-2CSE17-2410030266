def minSwaps(arr, k):
    n = len(arr)
    good = 0

    for num in arr:
        if num <= k:
            good += 1

    if good == 0 or good == n:
        return 0

    bad = 0
    for i in range(good):
        if arr[i] > k:
            bad += 1

    ans = bad

    for i in range(1, n - good + 1):
        if arr[i - 1] > k:
            bad -= 1
        if arr[i + good - 1] > k:
            bad += 1
        ans = min(ans, bad)

    return ans
