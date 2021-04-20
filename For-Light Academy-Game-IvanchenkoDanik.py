from random import randint
import os


def clrs():
    os.system('cls' if os.name == 'nt' else 'clear')  # now, to clear the screen


class Player:
    def __init__(self, hp=10, max_hp=10, pw=2, level=0, sp=5, xp=0, max_xp=100, heal_hp=5):
        self.hp = hp
        self.max_hp = max_hp
        self.pw = pw
        self.level = level
        self.sp = sp  # Skill points
        self.xp = xp
        self.max_xp = max_xp  # To going next level (max_xp) will multiply by 5
        self.heal_hp = heal_hp


def menu_upgrade(p):
    while p.sp > 0:  # While people has skill points > 0
        clrs()  # now, to clear the screen
        print(f'Choose your upgrades! Skill points: {p.sp}')
        print('---')
        print(f'1. HP {p.hp}/{p.max_hp}')
        print(f'2. Power {p.pw}')
        print(f'3. Heal points {p.heal_hp}')
        n = int(input('Число: '))
        if n == 1:
            p.hp += 5
            p.sp -= 1
            p.max_hp += 5
        if n == 2:
            p.pw += 1
            p.sp -= 1
        if n == 3:
            p.heal_hp += 1
            p.sp -= 1


def menu_stats(p):
    clrs()
    print('Player stats!\n')
    print(f'HP: {p.hp}/{p.max_hp}')
    print(f'Healing {p.heal_hp}')
    print(f'Power {p.pw}')
    input('Enter to continue.')


def menu_simple(p):
    while True:
        clrs()
        print('Choose what to do')
        print('1. Go fight')
        print('2. Check your stats')
        n = int(input('Число: '))
        if n == 1:
            menu_fight(p)
        if n == 2:
            menu_stats(p)


def menu_fight(p):
    ehp = 5 * randint(4, 20)
    epw = 2 * randint(1, 5)
    while ehp > 0:
        clrs()
        print(f'ENEMY: {ehp} Power: {epw}')
        print(f'You: {p.hp}/{p.max_hp} Power: {p.pw}')
        print('---')
        print(f'1. Punch with power {p.pw}')
        print(f'2. Heal (+{p.heal_hp})')
        print('3. Run away!')
        n = int(input('Число: '))
        if n == 1:
            r = randint(1, 2)
            if r == 1:
                ehp -= p.pw
                print('You hit the enemy!')
            if r == 2:
                p.hp -= epw
                print('Enemy hit you!')
                if p.hp < 0:
                    print('You loose')
                    return False
        if n == 2:
            p.hp += p.heal_hp
            if p.hp > p.max_hp:
                p.hp = p.max_hp
            print(f'Healing... {p.hp}')
        if n == 3:
            r = randint(1, 3)
            if r == 3:
                print('You ran away!')
                return True
            else:
                print("You can't run!")
    p.xp += 1
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1


p = Player()
menu_simple(p)
