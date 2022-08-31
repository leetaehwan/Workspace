class Person:
  def __init__(self, name,age,address):
      self.name = name
      self.age = age
      # self.address = address

  __slots__ = ['name', 'age']    # name, age만 허용(다른 속성은 생성 제한)

maria = Person('태환',33,'부천시')
maria.name = '마리아'                     # 허용된 속성
maria.age = 20                            # 허용된 속성
# maria.address = '서울시 서초구 반포동'    # 허용되지 않은 속성은 추가할 때 에러가 발생함

print(maria.name, maria.age)