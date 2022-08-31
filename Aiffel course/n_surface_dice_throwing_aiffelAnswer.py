from random import randrange

class FunnyDice:
  def __init__(self,n = 6):
    self.n = int(n)
    self.numbers = list(range(1, n+1))
    self.index = randrange(0,self.n)
    self.val = self.numbers[self.index]
  
  def throw(self):
    self.index = randrange(0,self.n)
    self.val = self.numbers[self.index]

  def getval(self):
    return self.val

  def setval(self, val:int):
    if val <= self.n:
      self.val = val
    else:
      msg = "It is not the Dice number. Dice has numbers of 1 ~ {0}".format(self.n)
      raise ValueError(msg)

def get_inputs():
  return int(input("주사위 면의 개수를 입력하세요: "))

n = get_inputs()
mydice = FunnyDice(n)
mydice.throw()
print("행운의 숫자는? {}".format(mydice.getval()))