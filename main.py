'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

'''
[4,1,2,1,2]
0  1 2 3 4

InterviewPrep
    Easy 
        SumOfThree 
          sumofthree.py
        BinHeap 
          binheap.py
    Medium
    Hard
'''

def findSingleNum(array):
  num_map = {}

  for value in array:
    if value not in num_map:
      num_map[value] = 1
    else:
      num_map[value] += 1

  smallest = float("inf")
  for key,value in num_map.items():
    if value == 1:
      smallest = key
      
  return smallest

# Approach 3: Bit Manipulation
def single_number(integers):
    result = 0
    for integer in integers:
        result = result ^ integer
    return result

nums = [2,2,1,1,1,4,4,3,55,55]
print(findSingleNum(nums))

'''
Approach 1: use another data structure to hold the numbers you have found.
Time complexity (if you use another array) may be up to O(n^2). If you use a hash table, you may be able to get up to O(n). 
Space complexity is O(n), which is not constant space.

Approach 2: use math and Set
Time complexity: likely O(n), as O(n + n) is really just O(n). The number of steps grows linearly.
Space complexity: O(n), as the addition will require the whole list to be duplicated.

Approach 3: Bit Manipulation
Time complexity: O(n)
Space complexity: O(1)
You'll have to look up this approach on your own - what kind of bitwise operations are there? What happens when you use them? 
The solution for this particular problem is easily found on google, so try looking up the Bitwise Operations in Python to try to work through it.
'''


'''
I am designing a media player that should store songs and play them in
random order. I need to be able to insert, delete, and play a random song.
What data structure would you use?
'''


https://www.rapidtables.com/tools/notepad.html

https://www.pacificcitizen.org/


http://mashdata-staging.khoalify.com/


http://archive.li/yEIJT