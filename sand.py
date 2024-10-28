"""
    Логика баффов и дебафов
"""
import datetime
import time

a = {'name': {('=', 'Amir'): {'hp': 100}}, 'hp': {('>', 6): {'strength': 10}, ('<', 100): {'strength': -20}}}
b = (2, (('name', '=', 'Amir'), ('hp', '>', 5)), (('strength', 'plus', 100),))
v = (1, (('name', '=', 'Amir'),), (('name', 'replace', 'РАБ'),))
x = (1, (('strength', '>', 1000),), (('strength', 'replace', 1_000_000),))

users = [
    {'name': 'Amir', 'hp': 10, 'strength': 12},
    {'name': 'LOH', 'hp': 2, 'strength': 12},
    {'name': 'Vitya', 'hp': 2, 'strength': 1200},
    {'name': 'lol', 'hp': 10, 'strength': 12}
    ]

me = {'name': 'Amir', 'hp': 2, 'strength': 12}


def add_buffs(user, enemy, buffs: dict[tuple: tuple]):
    terms = 0
    needed = buffs[0]
    for i in buffs[1]:
        match i[1]:
            case '=':
                if enemy[i[0]] == i[2]:
                    terms += 1
            case '>':
                if enemy[i[0]] > i[2]:
                    terms += 1
            case '<':
                if enemy[i[0]] < i[2]:
                    terms += 1
    if terms >= needed:
        for k in buffs[2]:
            match k[1]:
                case 'plus':
                    user[k[0]] += k[2]
                case 'minus':
                    user[k[0]] -= k[2]
                case 'replace':
                    user[k[0]] = k[2]
    return user


# while True:
#     t = int(input())
#     stat = me.copy()
#
#     start = time.time()
#     stat = add_buffs(stat, users[t], b)
#     stat = add_buffs(stat, users[t], v)
#     stat = add_buffs(stat, users[t], x)
#     print(time.time() - start)
#
#     print(stat)

b = 0

start = time.time()
for i in range(10_000_000):
    pass

print(time.time() - start)

b = 0
code = '''
for i in range(10_000_000):
    pass
'''

start = time.time()
exec(code)
print(time.time() - start)
