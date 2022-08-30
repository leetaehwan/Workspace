def fib(num):
  if num <= 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fib(num-2)+fib(num-1)



n = int(input())
print(fib(n))