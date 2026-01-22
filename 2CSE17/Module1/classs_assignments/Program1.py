#You are given an array of integer arr[].You have to reverse the given array.
class Solution:
    def reverseArray(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

obj = Solution()
arr = [1, 2, 3, 4]
result = obj.reverseArray(arr)
print("Reverse Array:", result)
