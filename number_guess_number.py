'''
secret number
guess a no. from 1- 10 = 5
hurray! you guesses it right
oh no! you guesses it wrong, no. was 3

'''
import random

secret_number=random.randint(1,10)
user_num=int(input("guess a number from 1 - 10 = "))
if user_num==secret_number:
    print("you guessed right")

else:
    print(f"you guess it wrong. the number was {secret_number}")



