import random
magic_number = random.randint(1,10)
num_guess = 1
while num_guess <= 3:
    user_guess = int(input("guess the number 1-10"))
    if user_guess == magic_number:
        print(f"{user_guess} You guessed it!")
        break
    elif user_guess > magic_number:
        print("Too high!")
        if num_guess == 3:
            print(f"No more attempts left. Num was {magic_number}")
    elif user_guess < magic_number:
        print("Too low!")
        if num_guess == 3:
            print(f"No more attempts left. Num was {magic_number}")
    num_guess += 1
print("Goodbye.")



# OR for i in range(3) # exclusive of 3, starting from 0
# OR use for...else
# outside the for... win = False
# inside the for... win = True if win
# outside the for at end of script
# if !win:
    #print("out of guesses")