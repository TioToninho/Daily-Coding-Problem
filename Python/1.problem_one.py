def sum_k(nums, k):
  # Scrolls through the list of numbers
  for num in nums:
    # Checks if the current number is the second number of the pair that adds up to k
    if k - num in nums:
      return True
  # If we have come this far, no pair has been found that sums to k
  return False

print(sum_k([10, 15, 3, 7], 17))  # Return True
print(sum_k([10, 15, 3, 7], 25))  # Return True
print(sum_k([10, 15, 3, 7], 19))  # Return False