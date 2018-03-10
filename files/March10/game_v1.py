class Character(object):
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print "%s does %d damage to the %s." % (self.name, enemy.power, enemy.name)
        if enemy.health <= 0:
            print "The goblin is dead." % enemy.name

    def print_status
class Hero(Character):
    def __init__(self):
        self.health = 10 #move to self #tells the class that it is related directlly to you
        self.power = 5
class Goblin(Character):
    def __init__(self):
         self.health = 6
         self.power = 2
    
    def attack(self, enemy):
    # Goblin attacks hero
            enemy.health -= self.power
            print "The goblin does %d damage to you." % self.power
            if enemy.health <= 0:
                print "You are dead."
    def print_status(self):
        print "You have %d health and %d power." % (self.health, self.power)

def main():
    barry_the_hero = Hero()
    steve_the_goblin = Goblin()

    while steve_the_goblingoblin.alive() and barry_the_hero.alive()
        barry_the_hero.print_status
        steve_the_goblin.print_status
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()

        if input == "1":
            # Hero attacks goblin
            barry_the_hero.attack(steve_the_goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if steve_the_goblin.alive > 0:
            


main()
