def merge(a, b):
    n = len(a)
    m = len(b)
    gap = (n + m + 1) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < n + m:
            if j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
            elif i < n:
                if a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]
            else:
                if b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]
            i += 1
            j += 1
        if gap == 1:
            gap = 0
        else:
            gap = (gap + 1) // 2
a = [2, 4, 7, 10]
b = [2, 3]
merge(a, b)
print(a)
print(b)
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
merge(a, b)
print(a)
print(b)
