from random import randint
from character import Character
from enemy import Enemy

class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.player=None
        self.state = 'normal'
        self.health = 10
        self.health_max = 10
        self.wealth=5

        self.Commands = {
            'explore': Player.explore,
            'flee': Player.flee,
            'attack': Player.attack,
            'quit': Player.quit,
            'help': Player.help,
            'status': Player.status,
            'rest': Player.attack,
        }
    def quit(self):
        print("%s fucked up finding the way back home, and yamraj came and took him to hell.\nR.I.P." % self.name)
        self.health = 0

    def help(self):


        print(self.Commands.keys())

    def status(self):
        print("%s's health: %d/%d, %s's wealth: %d" % (self.name, self.health, self.health_max,self.name,self.wealth))

    def tired(self):
        print("%s feels tired." % self.name)
        self.health = max(1, self.health - 1)

    def rest(self):
        if self.state != 'normal':
            print("%s can't rest now!" % self.name, self.enemy_attacks())
        else:
            print("%s rests." % self.name)

            if randint(0, 1):
                self.enemy = Enemy(self)
                print("%s is rudely awakened by, his spirit caught fire %s!" % (self.name, self.enemy.name))
                self.state = 'fight'
                self.enemy_attacks()
            else:
                if self.health < self.health_max:
                    self.health = self.health + 1
                else:
                    self.health = self.health - 1
                    print(self.name, 'slept too much.', self.health)

    def explore(self):
        if self.state != 'normal':
            print("%s is too busy right now!" % self.name)
            self.enemy_attacks()
        else:
            print("%s explores a golgol passage." % self.name)
            if randint(0, 1):
                self.enemy = Enemy(self)
                print("%s encounters %s!" % (self.name, self.enemy.name))
                self.state = 'fight'
            else:
                if randint(0, 1): self.tired()

    def flee(self):
        if self.state != 'fight':
            print("%s runs for a spaceship to go to mars ." % self.name, self.tired())
        else:
            if randint(1, self.health + 5) > randint(1, self.enemy.health):
                print("%s flees from %s." % (self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
            else:
                print("%s couldn't escape from %s!" % (self.name, self.enemy.name), self.enemy_attacks())

    def attack(self):
        if self.state != 'fight':
            print("%s swats the air, as if he is dusting the room (he is a total billa)." % self.name, self.tired())
        else:
            if self.do_damage(self.enemy):
                print("%s executes %s!" % (self.name, self.enemy.name))
                self.wealth=self.wealth+self.enemy.wealth
                self.enemy = None
                self.state = 'normal'
                if randint(0, self.health) < 10:
                    self.health = self.health + 1
                    self.health_max = self.health_max + 1
                    print("%s feels stronger and filled with the josh of mardangi!" % self.name)
            else:
                self.enemy_attacks()

    def enemy_attacks(self):
        if self.enemy.do_damage(self): print("%s was fucked %s!!!\nR.I.P." % (self.name, self.enemy.name))




