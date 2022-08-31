class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def is_time_valid(clr, tstr):
      if len(map(int,tstr.split(":"))) ==3:
        return True
      else:
        return False
    @staticmethod
    def from_string(tstr):
      


    
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')