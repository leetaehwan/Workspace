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

def means(nums):
  total = 0.0
  for i in range(len(nums)):
    total = total + nums[i]
  return total / len(nums)

def std_dev(nums, avg):
  total = 0.0
  for i in range(len(nums)):
    total = total + (nums[i] - avg)**2
  return (total / len(nums)) **0.5

X = numbers()

med = median(X)
avg = means(X)
std = std_dev(X,avg)

print(f'''당신이 입력한 숫자{X}의
  중앙값은 {med}, 평균은 {avg}, 표준편차는 {std}입니다.''')