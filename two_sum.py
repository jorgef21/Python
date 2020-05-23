"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(nums, target):
        h_table = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in h_table:
                return [h_table[diff], i]
            h_table[v] = i

def main():
    print(twoSum([2, 7, 11, 15],9))

if __name__=="__main__":
    main()