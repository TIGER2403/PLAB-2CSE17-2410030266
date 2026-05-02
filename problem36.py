def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

if __name__ == "__main__":
    print(plus_one([1,2,3]))  # [1,2,4]
    print(plus_one([4,3,2,1]))  # [4,3,2,2]
    print(plus_one([9]))  # [1,0]
