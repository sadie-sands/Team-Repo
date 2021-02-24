# Sadie Sands (sss4wz)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            try1 = target - i
            if try1 in nums[nums.index(i)+1:len(nums)]:
                answer_list=nums[nums.index(i)+1:len(nums)]
                answer = [nums.index(i), answer_list.index(try1)+nums.index(i)+1]
                return answer