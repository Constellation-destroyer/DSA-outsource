## Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 
Example 1:

Input: nums = [1,2,3,4,5] <br>
Output: true<br>
Explanation: Any triplet where i < j < k is valid.<br>

Example 2:

Input: nums = [5,4,3,2,1]<br>
Output: false<br>
Explanation: No triplet exists.<br>

Example 3:

Input: nums = [2,1,5,0,4,6]<br>
Output: true<br>
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.<br>
 

Constraints:

- 1 <= nums.length <= 5 * 10^5<br>
- -2^31 <= nums[i] <= 2^31 - 1<br>
