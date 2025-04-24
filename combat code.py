import random, time

class Character:
    def __init__(self, health, damage, stamina, mp):
        self.health = health
        self.damage = damage
        self.stamina = stamina
        self.mp = mp

    def heal(self, target):
        heal_amount = 30
        target.health += heal_amount
        if target.health > 100:
            target.health = 100

    def take_damage(self):
        for i in range(10):
            damage_taken = random.randint(1, 6)
            self.health -= damage_taken
            print(f"character takes {damage_taken} damage. New health: {self.health}")
            time.sleep(1)

    def mp_used(self):
        mp_used = random.randint(1,10)
        self.mp -= mp_used
        print(f"character has {self.mp} left")
        time.sleep(1)

    def attack(self):
        if Character.stamina < 0:
            enemy1.take_damage()


warrior = Character(120, 30, 40, 30)
theif = Character(100, 20, 50, 40)
healer = Character(75, 10, 30, 50)
mage = Character(100, 30, 30, 100)

enemy1 = Character(100, 20, 20, 5)
enemy2 = Character(75, 25, 20, 10)
enemy3 = Character(50, 15, 20, 5)
enemy4 = Character(75, 20, 20, 15)
