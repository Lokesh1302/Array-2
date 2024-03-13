# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Time Complexity : O(log(N))
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None


# Your code here along with comments explaining your approach in three sentences only
# Approach : We iterate over the elements of the array and add them to the hashset.
# Then we iterate over the target elements and check if it exists in the set or not. If not add it to the result.


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_set = set()
        for cur in nums:
            hash_set.add(cur)

        result = []
        for index in range(1, len(nums) + 1):
            if index not in hash_set:
                result.append(index)

        return result