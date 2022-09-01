class Calculator:
  add = 0
  sub = 0
  mul = 0
  div = 0

  def Add(self,num,antnum):
    self.add += 1
    return num + antnum

  def Sub(self,num,antnum):
    self.minus += 1
    return num - antnum

  def Mul(self,num,antnum):
    self.mul += 1
    return num * antnum

  def Div(self,num,antnum):
    self.div += 1
    return num / antnum
  
  
  def ShowCount(self):
    print(f'''
덧셈 : {self.add}
뺄셈 : {self.sub}
곱셈 : {self.mul}
나눗셈 : {self.div}
''')

cal = Calculator()
print("10 + 20 = %s" %cal.Add(10,20))
print("10 * 10 = %s" %cal.Mul(10,10))
print("10 * 10 = %s" %cal.Mul(10,15))

cal.ShowCount()