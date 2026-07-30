# Question 16(a)
# Examination Number: 
from random import randint

def guess_game(max_guesses_allowed):
    
    secret_number = randint(1,5)
    guess_count = 0
    user_guess = 0
    level=0
    guesses=[]
    
    #part i & ii & iii
    level=input("Enter difficulty E(asy) or H(ard): ")
    if level =="H":
        secret_number = randint(1,100)
    else:
        secret_number = randint(1,5)
    
    
    while (user_guess != secret_number)and(guess_count<max_guesses_allowed):
        
        user_guess = int(input("Enter your guess: "))
        
        
        guess_count += 1   #Increase guess_count by 1
        
        if user_guess == secret_number:
            print("Congratulations! You win!")
            print("you took",guess_count,"guesses.")
            
        elif user_guess>secret_number:
            print("Sorry! Your guess was too high")
            if user_guess in guesses:
                print("You already guessed this number")
            guesses.append(user_guess)
        elif user_guess<secret_number:
            print("Sorry! Your guess was too low")
            if user_guess in guesses:
                print("You already guessed this number")
            guesses.append(user_guess)
                    
#iv
print("Welcome to the guessing game!")
max_guesses= int(input("Enter the maximum number of guesses allowed: "))
guess_game(max_guesses)