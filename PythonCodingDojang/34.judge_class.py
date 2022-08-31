class Annie:
  def __init__(self,health,mana,ability_power):
    self.health = health
    self.mana = mana
    self.ability_power = ability_power

  def tibbers(self):
    n = self.ability_power
    print(f'티버: 피해량 {n*0.65+400}')

health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()