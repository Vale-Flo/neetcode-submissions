class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return (-1)

        #Binary search
        #solution optimised cause O(log n)

        izq = 0
        der = len(nums)-1

        #the values are already in ascending order
        # for i in range(len(nums)):
        while izq <= der:
            found = (izq+der)//2
            if nums[found] < target:
                izq = found + 1
            elif nums[found] > target:
                der = found - 1
            elif nums[found] == target:
                return (found)
        
        return -1

