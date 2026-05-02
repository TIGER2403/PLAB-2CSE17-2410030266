def allPalindromes(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True
