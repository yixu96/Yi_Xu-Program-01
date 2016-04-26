import random

class Treasure:
    # weapon = ['gun', 'long sword', 'short sword']
    # food = ['rice', 'noodles', 'apple', 'banana', 'meat', 'soup']
    # armor = ['chainmail', 'mail', 'gold chainmeil', 'helmet']
    # task_item = ['mail', 'book', 'a bottle of wine', 'bottle']
    # type = ['weapon', 'food', 'armor', 'gold']

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.inventory = []
        self.gold = 0
        self.on_body = []


    def pickup(self, treasure):
        if treasure != 'gold':
            self.inventory.append(treasure)    #'function' object has no attribute 'append' ????????????
        else:
            self.gold += 1

    def drop(self, location, treasure):    #????
        self.location = location
        if treasure in self.on_body:
            self.remove(treasure) or self.unwield(treasure)
        self.inventory.remove(treasure)

    def wear(self, armor):
        self.on_body.append(armor)
        self.inventory.remove(armor)

    def remove(self, armor):
        self.on_body.remove(armor)
        self.inventory.append(armor)

    def wield(self, weapon):
        self.on_body.append(weapon)
        self.inventory.remove(weapon)

    def unwield(self, weapon):
        self.on_body.remove(weapon)
        self.inventory.append(weapon)

    def eat(self, food):
        self.inventory.remove(food)

    def lookat(self):
        print('%s : %s', self.name, self.type)



class Player(Treasure):
    def __init__(self, pname, attackl, defensel, healthl, experiencel, position):
        self.pname = pname
        self.attackl = attackl
        self.defensel = defensel
        self.healthl = healthl
        self.experiencel = experiencel
        self.position = position

    def look_at(self):
        print('an adventurer named %s, attack level: %s, defense level: %s, health level: %s, experience level: %s', self.name, self.attackl, self.defensel, self.healthl, self.experiencel)

    def move_to(self, position):
        self.position = position

    def inventory(self):
        for a in range(len(self.on_body)):
            print(a + '. a %s', self.name)
        for b in range(len(self.inventory)):
            print(b + '. a %s', self.name)
        print(str(self.gold) + ' gold coins')

    def equip(self):
        for i in self.inventory:
            self.wear(i) or self.unwield(i)

    def remove(self, armor):
        self.remove(armor)
        print('%s removed.', armor)

    def unwield(self, weapon):
        self.unwield(weapon)
        print('%s unwielded', weapon)

    def eat(self, index):
        self.eat(self.inventory[index])

    def drop(self, index):
        self.drop(self.inventory[index])



# 1.
def random_level():
    width = random.randint(10, 40)
    height = random.randint(10, 25)
    level = [['.' for w in range(width)] for h in range(height)]

    for w in range(width):
        level[0][w] = '#'
        level[-1][w] = '#'

    for h in range(height):
        level[h][0] = '#'
        level[h][-1] = '#'
    return level

print(random_level())

# 2.
levels = []
levels.append(random_level())
levels.append(random_level())
levels.append(random_level())
levels.append(random_level())
levels.append(random_level())
print(levels)

def up_level(level_num):
    if level_num == 1:
        print('out of the world. game ends.')
    else:
        level_num -= 1
    return level_num

def down_level(level_num):
    level_num += 1
    if level_num > len(levels):
        levels.append(random_level())
    return level_num

print(up_level(1))
print(down_level(5))
print(len(levels))

# 3.
def treasure_add(levels):
    for l in range(len(levels)):
        level = levels[l]
        if l%2 == 1:
            level[2][2] = 'u'
            level[-2][-2] = 'd'
        else:
            level[2][2] = 'd'
            level[-2][-2] = 'u'

        n = 0
        for i in level:
            for j in i:
                if j == '#' or 'u' or 'd':
                    n += 1

        r = random.randint(0, n)

        for k in range(1, r+1):
            row = random.randint(0, len(level)-1)
            column = random.randint(0, len(level[0])-1)

            if level[row][column] == 0:
                level[row][column] = '*'
    return levels

print(treasure_add(levels))  #一堆treasure那个dictiona怎么弄

# 4.
def action(command, player, treasure, index):
    if command == 'h':
        player.position[1] -= 1
    elif command == 'j':
        player.position[2] += 1
    elif command == 'k':
        player.position[2] -= 1
    elif command == 'l':
        player.position[1] += 1
    elif command == '^':
        player.position[0] -= 1
    elif command == 'v':
        player.position[2] += 1
    elif command == 'i':
        print(player.inventory)
    elif command == 'E':
        player.equip()
    elif command == 'a':
        player.wear(index)
    elif command == 'A':
        player.remove()
    elif command == 'w':
        player.wield(index)
    elif command == 'W':
        player.unwield()
    elif command == 'e':
        player.eat(index)
    elif command == 'd':
        player.drop(index)
    elif command == 'p':
        player.pickup(t.name)
    elif command == '?':
        print('• h: move to the left (West)\n'
              '• j: move down (South)\n'
              '• k: move up (North)\n'
              '• l: move to the right (East)\n'
              '• ˆ: take stairs up,• v: take stairs down\n'
              '• i: print the inventory\n'
              '• E: equip\n'
              '• a <index>: wear armor\n'
              '• A: remove armor\n'
              '• w <index>: wield weapon\n'
              '• W unwield\n'
              '• e <index>: eat an item\n'
              '• d <index>: drop an item\n'
              '• p <index>: pick up an item (the index referring to the pile of treasure the player stands on top of)\n'
              '• ?: print the list of possible commands')

    return Player

p = Player('Xuer', 90, 67, 100, 20, [1, 2, 2])
t = Treasure('apple', 'food')
com = 'h'
# com = '?'
# Player.lookat(t)

i = 0
print(action(com, p, t, i))

# 5.
class Enemy(Treasure):
  def __init__(self, player):
    self.mname = 'Monkey King'
    self.healthl = random.randint(1, player.healthl)

  def treasure(self):
    self.name = 'sword'
    self.type = 'weapon'


def do_damage(self, enemy):
    damage = min(max(random.randint(0, self.healthl) - random.randint(0, enemy.healthl), 0), enemy.healthl)
    enemy.healthl = enemy.healthl - damage
    if damage == 0:
        print('Attack aoided.')
    else:
        print('%s -%d', enemy.mname, damage)
    return enemy.healthl

enemy = Enemy(p)
while(enemy.healthl > 0):
    do_damage(p, enemy)

print('%s is dead. You win!', enemy.mname)
p.pickup(enemy.treasure)
