class Solution:
    def findMinMax(self,arr):
        min=arr[0]
        max=arr[0]

        for num in arr:
            if num<min:
                min=num
            if num>max:
                max=num
        return [min,max]

arr=[23,34,7,3,1,4,6,8,10,35]
obj =Solution()
result=obj.findMinMax(arr)
print("Array:",arr)
print("Min:",result[0])
print("Max:",result[1])