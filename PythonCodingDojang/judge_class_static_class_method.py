class Time:
  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second

  @staticmethod
  def is_time_valid(tstr):
    if 
  
  def from_string(self, tstr):
    self.tstr = tstr
    


time_string = input()
 
if Time.is_time_valid(time_string):
  t = Time.from_string(time_string)
  print(t.hour, t.minute, t.second)
else:
  print('잘못된 시간 형식입니다.')