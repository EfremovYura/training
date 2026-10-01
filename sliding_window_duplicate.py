"""
219. Contains Duplicate II  (leetcode)

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """
    Runtime 47 ms Beats 65.67%
    Memory 39.49 MB Beats 15.34%
    Current complexity: O(N)
    Suggested complexity: O(N)
    Suggestions: Perfectly optimal time complexity. Clean and efficient implementation!
    """

    num_dict = {}
    for i, num in enumerate(nums):

        if num in num_dict and i - num_dict[num] <= k:
            return True
        else:
            num_dict[num] = i

    return False


if __name__ == "__main__":
    assert containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    assert containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    assert containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
    print("passed")
