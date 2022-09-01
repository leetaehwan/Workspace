total = 0
count = 0

numbers = input("Enter a number : (<Enter Key> to quit)")
while numbers != '':
  try:
    x = float(numbers)
    count += 1
    total = total + x
  except ValueError:
    print("NOT a number! Ignored..")
  numbers = input("Enter a number : (<enter Key> to quit)")
avg = total / count
print("\n average is", avg)