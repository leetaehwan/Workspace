import numpy as np

def numbers():
  X = []
  number = input("Enter a number (<Enter key> to quit)")

  while number != "":
    try:
      x = float(number)
      X.append(x)
    except ValueError:
      print('>>> NOT a number! Ignored..')
    number = input("Enter a number (<Enter key> to quit)")
  return X

def main():
  nums = numbers()
  num = np.array(nums)
  print("합", num.sum())
  print("평균값", num.mean())
  print("표준편차",num.std())
  print("중앙값",np.median(num))

main()
