'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''    

def two_sum(nums, target):
  hash_table = {}
  for num in nums:
    hash_table[num] = num
  # print(hash_table)

  for i in hash_table:
    
    for j in hash_table:
      if hash_table[i] + hash_table[j] == target and hash_table[i] != hash_table[j]:
        return print(f'[index: {hash_table[i]}, {hash_table[j]}]')
      else: 
        j += 1

        


two_sum([3,2,4], 6)