# class Person:
#   def greeting(self):
#     print('Hello')

#   def hello(self):
#     self.greeting()

# james = Person()
# james.hello()

# # Check instance and class
# print(isinstance(james, Person))

# def factorial(n):
#   if not isinstance(n, int) or n< 0:
#     return None
#   if n == 1:
#     return 1
#   return n * factorial(n-1)

# print(factorial(6))

class Person:
  def __init__(self):
    self.hello = '안녕하세요.'
  def greeting(self):
    print(self.hello)

james = Person()
james.greeting()