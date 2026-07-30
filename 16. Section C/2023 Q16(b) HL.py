#Question 16B
# Exam Number:

from random import randint

user_score=0
secret_number= randint(1,100)
play_again="Y"


while play_again== "Y":
    user_guess= int(input("Enter your guess:"))
    difference= secret_number-user_guess

    print("Secret number is", secret_number,". You guessed", user_guess, ". Difference is", difference)

    if user_guess==secret_number:
        user_score=user_score+100
        print("JACKPOT!! You score 100 points")
    elif difference<20 and difference>-20:
        user_score=user_score+20
        print("You score 20 points")
    else:
        user_score=user_score-30
        print("You lose 30 points")
        
    print("Your score is:", user_score)
    play_again= input("Play again? (Y/N):")

