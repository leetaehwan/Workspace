def numbers():
  X = []
  while True:
    number = input("Enter a number (<Enter key> to quit)")
    while number != "":
      try:
        x = float(number)
        X.append(x)
      except ValueError:
        print('>>> NOT a number! Ignored..')
      number = input("Enter a number (<Enter key> to quit)")
    if len(X) > 1:
      return X

def median(nums):
  nums.sort()
  size = len(nums)
  p = size//2
  if size % 2 ==0:
    pr = p
    pl = p-1
    mid = float((nums[pl]+nums[pr])/2)
  else:
    mid = nums[p]
  return mid

X = numbers()

print('X :', X)
print(median(X))
