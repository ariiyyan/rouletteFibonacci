import random


INITIAL_BET = 5


totalNumGame = int(input("how many times do you want to play: "))
money = int(input("how much money you have to start the game: "))

num1 = 5
num2 = 5
temp = 0
count = totalNumGame

won_count = 0
while money > 0 and count > 0:
    count -= 1
    num = random.randint(0, 36)
    bet_on_odd = random.choice([True, False])
    if (num % 2 == 0 and num != 0 and num != 36 and bet_on_odd is False) or (num % 2 == 1 and num != 0 and num != 36 and bet_on_odd is True):
        money += num2
        if num2 != INITIAL_BET:
            temp2 = num2
            num2 = num1
            num1 = temp2 - num1
            temp2 = num2
            num2 = num1
            num1 = temp2 - num1
        won_count += 1
        print(f"Won, number of roulette is = {num} and total money is = {money} and the bet for next hand is = {num2}")
    else:
        money -= num2
        temp = num2
        num2 = num1 + num2
        num1 = temp
        print(f"Lost, number of roulette is = {num} and total money is = {money} and the bet for next hand is = {num2}")

print(f" {totalNumGame} many time played happen")
print(f"Number of times won: {won_count}")
print(f" total money left is  =  {money}")