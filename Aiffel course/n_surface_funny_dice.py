# Definition of FunnyDice class
# Feature
# 1. Input number of dice's surface
# 2. Print Random number of dice throwing


import random as rd

class FunnyDice:
  def __init__(self, n=int(input())): # Feature 1
    self.n = n

  def throw(self): # Feature 2
    n = self.n
    print(rd.randint(1,n))

dice = FunnyDice()

dice.throw()