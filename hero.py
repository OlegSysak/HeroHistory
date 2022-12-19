from time import sleep

class Jojo():

    def __init__(self, name, health, armor, power, weapon, special, megapover, vievmagic , magiceffect):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special
        self.megapover = megapover
        self.vievmagic = vievmagic
        self.magiceffect = magiceffect

    #def print_info(self):
        #print("New hero!!! Fast ", self.name)
        #print("New hero!!! Fast ", self.health)
        #print("and lite armor", self.armor)
        #print("His mega power ", self.power)
        #print("MegaPower", self.weapon)
        #print("MegaPower", self.special)

    def print_info(self):
        #sleep(1)
        print("*Kingdom of Chrom*")
        #print("Hero name is ", self.name)
        #sleep(1)
        #print("Health:", self.health)
        #sleep(1)
        #print("Armor:", self.armor)
        #sleep(1)
        #print("Power:", self.power)
        #sleep(1)
        #print("Weapon:", self.weapon)
        #sleep(1)
        #print("Special:", self.special)
        #sleep(1)

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)


    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "felt in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "felt in battle")
                break

    def super(self, enemy):
        print("Hero", self.name, "Super attack", self.special, enemy.name)
        enemy.armor = enemy.armor - self.megapover
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def seriouls(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.super(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.super(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def effect(self, enemy):
        print("Hero", self.name, "Using magic", self.vievmagic, enemy.name)
        enemy.armor = enemy.armor - self.magiceffect
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def magic(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.effect(enemy)
            if enemy.health <= 0:
                print(enemy.name, "AAAA")
                break
            enemy.effect(self)
            if self.health <= 0:
                print(self.name, "AAAAAA")
                break


class Arsen():

    def __init__(self, name, health, armor, power, weapon, special, megapover, vievmagic , magiceffect):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special
        self.megapover = megapover
        self.vievmagic = vievmagic
        self.magiceffect = magiceffect

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)


    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "felt in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "felt in battle")
                break

    def super(self, enemy):
        print("Hero", self.name, "Super attack", self.special, enemy.name)
        enemy.armor = enemy.armor - self.megapover
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def seriouls(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.super(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.super(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def effect(self, enemy):
        print("Hero", self.name, "Using magic", self.vievmagic, enemy.name)
        enemy.armor = enemy.armor - self.magiceffect
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def magic(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.effect(enemy)
            if enemy.health <= 0:
                print(enemy.name, "AAAA")
                break
            enemy.effect(self)
            if self.health <= 0:
                print(self.name, "AAAAAA")
                break

class Diawollo():
    def __init__(self, name, health, armor, power, weapon, special, megapover, vievmagic , magiceffect):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special
        self.megapover = megapover
        self.vievmagic = vievmagic
        self.magiceffect = magiceffect
    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)


    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "felt in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "felt in battle")
                break

    def super(self, enemy):
        print("Hero", self.name, "Super attack", self.special, enemy.name)
        enemy.armor = enemy.armor - self.megapover
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def seriouls(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.super(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.super(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def effect(self, enemy):
        print("Hero", self.name, "Using magic", self.vievmagic, enemy.name)
        enemy.armor = enemy.armor - self.magiceffect
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def magic(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.effect(enemy)
            if enemy.health <= 0:
                print(enemy.name, "AAAA")
                break
            enemy.effect(self)
            if self.health <= 0:
                print(self.name, "AAAAAA")
                break

class Tooru():

    def __init__(self, name, health, armor, power, weapon, special, megapover):
            self.name = name
            self.health = health
            self.armor = armor
            self.power = power
            self.weapon = weapon
            self.special = special
            self.megapover = megapover

    def strike(self, enemy):
            print("Tooru", self.name, "Super attack", enemy.name)
            enemy.armor = enemy.armor - self.power
            if enemy.armor <= 0:
                enemy.health = enemy.health + enemy.armor
                enemy.armor = 0
            print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
            while self.health > 0 and enemy.health > 0:
                self.strike(enemy)
                if enemy.health <= 0:
                    print(enemy.name, "die in battle")
                    break
                enemy.strike(self)
                if self.health <= 0:
                    print(self.name, "die in battle")
                    break

    def super(self, enemy):
        print("Hero", self.name, "attacking", self.special, enemy.name)
        enemy.armor = enemy.armor - self.megapover
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def seriouls(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.super(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.super(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

class King():

    def __init__(self, name, health, armor, power, weapon, special):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special

    #def print_info(self):
        #print("New hero!!! Fast ", self.name)
        #print("New hero!!! Fast ", self.health)
        #print("and lite armor", self.armor)
        #print("His mega power ", self.power)
        #print("MegaPower", self.weapon)
        #print("MegaPower", self.special)

    #def print_info(self):
        #sleep(1)
        #print("New hero!!!")
        #sleep(1)
        #print("Hero name is ", self.name)
        #sleep(1)
        #print("Health:", self.health)
        #sleep(1)
        #print("Armor:", self.armor)
        #sleep(1)
        #print("Power:", self.power)
        #sleep(1)
        #print("Weapon:", self.weapon)
        #sleep(1)
        #print("Special:", self.special)
        #sleep(1)

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

class Woolfs():

    def __init__(self, name, health, armor, power, weapon, special):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special


    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

class Kaban():

    def __init__(self, name, health, armor, power, weapon, special, vievmagic , magiceffect):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special
        self.vievmagic = vievmagic
        self.magiceffect = magiceffect

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def effect(self, enemy):
        print("Hero", self.name, "Using magic", self.vievmagic, enemy.name)
        enemy.armor = enemy.armor - self.magiceffect
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def magic(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.effect(enemy)
            if enemy.health <= 0:
                print(enemy.name, "AAAA")
                break
            enemy.effect(self)
            if self.health <= 0:
                print(self.name, "AAAAAA")
                break

class Bandit():

    def __init__(self, name, health, armor, power, weapon, special, vievmagic , magiceffect):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special
        self.vievmagic = vievmagic
        self.magiceffect = magiceffect

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def effect(self, enemy):
        print("Hero", self.name, "Using magic", self.vievmagic, enemy.name)
        enemy.armor = enemy.armor - self.magiceffect
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def magic(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.effect(enemy)
            if enemy.health <= 0:
                print(enemy.name, "AAAA")
                break
            enemy.effect(self)
            if self.health <= 0:
                print(self.name, "AAAAAA")
                break


class BanditBoss():

    def __init__(self, name, health, armor, power, weapon, special, megapover, vievmagic , magiceffect):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special
        self.vievmagic = vievmagic
        self.magiceffect = magiceffect
        self.megapover = megapover

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def super(self, enemy):
        print("Hero", self.name, "Super attack", self.special, enemy.name)
        enemy.armor = enemy.armor - self.megapover
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def seriouls(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.super(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.super(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def effect(self, enemy):
        print("Hero", self.name, "Using magic", self.vievmagic, enemy.name)
        enemy.armor = enemy.armor - self.magiceffect
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def magic(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.effect(enemy)
            if enemy.health <= 0:
                print(enemy.name, "AAAA")
                break
            enemy.effect(self)
            if self.health <= 0:
                print(self.name, "AAAAAA")
                break

class David():

    def __init__(self, name, health, armor, power, weapon, special, megapover, vievmagic , magiceffect):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.special = special
        self.vievmagic = vievmagic
        self.magiceffect = magiceffect
        self.megapover = megapover

    def strike(self, enemy):
        print("Hero", self.name, "attacking", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def super(self, enemy):
        print("Hero", self.name, "Super attack", self.special, enemy.name)
        enemy.armor = enemy.armor - self.megapover
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def seriouls(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.super(enemy)
            if enemy.health <= 0:
                print(enemy.name, "die in battle")
                break
            enemy.super(self)
            if self.health <= 0:
                print(self.name, "die in battle")
                break

    def effect(self, enemy):
        print("Hero", self.name, "Using magic", self.vievmagic, enemy.name)
        enemy.armor = enemy.armor - self.magiceffect
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "armor: ", enemy.armor, "and health", enemy.health)

    def magic(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.effect(enemy)
            if enemy.health <= 0:
                print(enemy.name, "AAAA")
                break
            enemy.effect(self)
            if self.health <= 0:
                print(self.name, "AAAAAA")
                break

