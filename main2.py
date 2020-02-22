'''
Maximum Subset Sum With No Adjacent Elements
input: [75, 105, 120, 75, 90, 135]
output: 330 ( 75 , 120 , 135)

1) 75 + 120 + 90
2) 75 + 75 + 135
3) 105 + 75 + 135

[75, 105, 120, 75, 90, 40]
max(75 + 120 , 105)

[75, 105, 195, 195, 285, max(40 + 195, 285) ]

[75, 105, 195, 195, 90 + 195(285), 135 + 195 = 330]


def maxSubsetSumNoAdjacent(array):
  max = 0

  for i in range(len(array)):
    if array[i] > max:
      max = array[i]
    sum = helper(array, max, i)
  
  return max

def helper(array, max, idx):
  idx2 = idx + 2
  for i in range(idx2, len(array)-1):
      sum = array[idx] + array[idx2]
      if sum > max:
        max = sum
      helper(array, max, idx2)


def maxSubsetSumNoAdjacent2(array):

  if len(array) == 0:
    return 0
  elif len(array) == 1:
    return array[0]
  else:
    max_sums = array[:]
    max_sums[1] = max_sums[0] if max_sums[0] > max_sums[1] else max_sums[1]

    for index in range(2, len(max_sums)): 
      max_sums[index] = max(max_sums[index - 1], max_sums[index - 2] + max_sums[index])
    return max_sums[-1]

# ​def maxSubsetSumNoAdjacent3(array):
#     if not len(array):
#         return 0
#     elif len(array) == 1:
#         return array[0]
#     second = array[0]
#     first = max(array[0], array[1])
#     for i in range(2, len(array)):
#         current = max(first, second + array[i])
#         second = first
#         first = current
#     return first

nums = [75, 105, 120, 75, 90, 135]
#                  ^  ^   i

print(maxSubsetSumNoAdjacent2(nums)) #330

http://archive.li/yEIJThttp://archive.li/yEIJT
'''