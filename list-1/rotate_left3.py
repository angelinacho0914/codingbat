def rotate_left3(nums):
  '''
  Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
  '''
  answer = []
  i = 0
  if i != len(nums)-1:
    for i in range(len(nums)-1):
      answer.append(nums[i+1])
  answer.append(nums[0])
  return answer