def max_area(height):
  left = 0
  right = len(height) - 1
  best = 0
  while left < right:
    distance = right - left
    shortest = min(height[left], height[right])
    current_water = distance * shortest
    if current_water > best:
      best = current_water

    if height[left] < height[right]:
      left += 1
    else:
      right -= 1
  return best
print(max_area([2, 8, 6, 4, 7]))
