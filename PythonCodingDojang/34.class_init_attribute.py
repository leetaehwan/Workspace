class Person:
  def __init__(self, name, age, address):
    self.hello = "안녕하세요."
    self.name = name
    self.age = age
    self.address = address

  def greeting(self):
    print(f'{self.hello} 저는 {self.name}입니다.')

maria = Person('마리아',20,'서울시 서초구 반포동')
maria.greeting()

print('이름', maria.name)
print('나이', maria.age)
print('주소', maria.address)