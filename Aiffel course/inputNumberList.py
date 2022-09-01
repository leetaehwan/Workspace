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



X = numbers()

print('X :', X)