class Car:
  color = 'red'
  category = 'sports car'

  def drive(self):
    print("I'm driving")

  def accel(self, speed_up, current_speed = 10):
    self.speed_up = speed_up
    self.current_speed = current_speed + speed_up
    print("speed up", self.speed_up, "driving at", self.current_speed)
class Car2:
  def __init__(self, color='red', category='sports car'):
    self.color = color
    self.category = category

  def drive(self):
    print("I'm driving")

  def accel(self, speed_up, current_speed = 10):
    self.speed_up = speed_up
    self.current_speed = current_speed + speed_up
    print("speed up", self.speed_up, "driving at", self.current_speed)

class NewCar(Car2):
  def __init__(self, color, category, maker):
    super().__init__(color,category)
    self.maker = maker


mycar = Car()
car2 = Car2('yellow','sedan')

print(mycar.color)

mycar.drive()
mycar.accel(5)

Car.drive(mycar)
print(car2.color)

newCar = NewCar('red','sports car',"Kia")
print(newCar.maker)