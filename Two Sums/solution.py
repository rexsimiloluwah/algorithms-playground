# SOLUTION FOR THE SIMPLE TWO SUMS PROBLEM 
# Time Complexity => O(n)

class Solution:

    @staticmethod
    def twoSum(nums, target):
        """
        Args 
        --------------------------------------------------
        nums (list) :- List of Numbers 
        target (int) :- Target for the addition

        Returns 
        --------------------------------------------------
        List of indices of the two numbers in nums that add up to the specified target i.e [0,1]
        """

        stateMap = {}
        for index, num in enumerate(nums):
            d = target - num
            if d in stateMap:
                return ([stateMap[d], index])
            stateMap[num] = index

    @staticmethod
    def twoSumReturnsNumbers(nums, target):
        state = []
        for i in nums:
            d = target - i
            if d in state:
                return ([d, i])
            state.append(i)

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,5,7,11,15], 9))
# Returns [0,2] since 2 + 7 = 9 AND they are at index 0 and 2 respectively

