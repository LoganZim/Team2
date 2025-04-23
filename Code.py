class Character:
    def __init__(self, maxhealth, damage, speed, iq, strength,armor):
        self.maxhealth = maxhealth
        self.damage = damage
        self.speed = speed
        self.iq = iq
        self.strength = strength
        self.armor = armor
class Armor:
    def __init__(self, iqReq, strengthReq, ):
name=""
warrior = Character(750, 55, 50,90,175,0)
thief = Character(600, 30, 70,110,120,0)
wizard = Character(500, 100, 40,160,100,0)

def first_apperance():
    print('Hello welcome to your adventure')
    input('Who would you like to be known as: ')

first_apperance()
