class Character:
    def __init__(self, maxhealth, damage, speed, iq, strength, armor, health, magic):
        self.maxhealth = maxhealth
        self.damage = damage
        self.speed = speed
        self.iq = iq
        self.strength = strength
        self.armor = armor
        self.health = health
        self.magic = magic

    def dmgBuff(self):
        self.damage+=50
class Enemy:
    def __init__(self, maxhealth, damage, speed, iq, strength, armor, health, magic):
        self.maxhealth = maxhealth
        self.damage = damage
        self.speed = speed
        self.iq = iq
        self.strength = strength
        self.armor = armor
        self.health = health
        self.magic = magic

#Characters
warrior = Character(750, 100, 50,90,175,20,750,0)
thief = Character(600, 80, 70,110,120,10,600,0)
wizard = Character(500, 130, 40,160,100,20,500,100)

#enemies
wolf = Character(350, 80, 90,100,45,10,350,0)
bear = Character(800, 100, 70,100,100,50, 800,0)
troll = Character(850, 150, 50,100,150,50, 850,0)
dark_entity = Character(1500, 150, 60, 300, 5000, 20, 1500, 150)


def first_apperance():
    print('Hello welcome to your adventure')
    name = input('Who would you like to be known as: ')
    choice = int(input('ok',name,'now what would you like to be, warrior(1) thief(2) or wizard(3): '))
    if choice == 1:
        warriorJourney()
    if choice == 2:
        thiefJourney()
    if choice == 3:
        wizardJourney()

def warriorJourney():

def thiefJourney():

def wizardJourney():

first_apperance()
