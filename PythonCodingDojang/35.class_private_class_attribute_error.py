class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def is_time_valid(cls,tstr):
      if len(list(map(int,tstr.split(":")))) ==3:
        hour, minute, second = map(int,tstr.split(":"))
        if hour <= 24 and minute < 60 and second < 60:
          return True
        else:
          return False 
      else:
        return False
    @classmethod
    def from_string(cls,tstr):
      hour, minute, second = map(int,tstr.split(":"))
      s = cls(hour, minute, second)
      return s
       
    
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')