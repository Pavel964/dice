import random
player = random.randint(1, 32) # кидаем кости от 1 до 32
cpu = random.randint(1, 32) # кидаем кости от 1 до 32

print("Игрок кинул", player) # печатаем кости игрока
print("компьютер кинул", cpu) # печатаем кости компа

if player > cpu:
    print("Игрок победил!")
elif cpu > player:
    print("комп победил!")
else:
    print("Ничья!")