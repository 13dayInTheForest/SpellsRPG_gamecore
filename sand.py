import random
karma = random.randint(0, 20)
strength = random.randint(0, 20)
mana = random.randint(0, 20)

print(karma, strength,mana)
if karma < 5 and mana < 5 and strength < 5:
    print('sad')