def binary_search(num, target):

  left_index  = 0
  right_index = len(num) - 1

  while (left_index < right_index):
    print(left_index, right_index)
    mid_index = int((right_index - left_index) / 2)
    current_index = left_index + mid_index

    current_value = num[current_index]

    if (current_value == target):
       return current_index

    if (current_value > target):
       right_index = mid_index
    else:
       left_index = mid_index

  return -1



num = [0, 1, 2, 3, 4, 5 ]
target = 0

result = binary_search(num, target)
print (result)
