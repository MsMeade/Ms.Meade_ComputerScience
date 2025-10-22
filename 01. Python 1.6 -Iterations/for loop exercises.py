# Example
# value = int(input("Please enter a positive value: "))
# 
# for i in range(1,value,2):
#     print(i)

#35
# name=input("please enter your name: ")
# 
# for i in range(3):
#     print(name)

#36
# name=input("please enter your name: ")
# num= int(input("Please enter a number: "))
# 
# for i in range(num):
#     print(name)
    
#37
# name=input("please enter your name: ")
# for letter in name:
#     print(letter)

#38
# name=input("please enter your name: ")
# num= int(input("Please enter a number: "))
# 
# for i in range(num):
#     for letter in name:
#         print(letter)

#39
# num= int(input("Please enter a number between 1 and 12: "))
# for i in range(12):
#     print(num*i)

#40
# num = int(input("Please enter a number below 50."))
# for i in range(50,(num-1),-1):
#     print(i)

#41
# name=input("please enter your name: ")
# num= int(input("Please enter a number: "))
# 
# if num<10:
#     for i in range(num):
#         print(name)
# else:
#     for i in range(3):
#         print("Too high!!!")

#42
# total =0
# for i in range(5):
#     num= int(input("Please enter a number: "))
#     decision= input("Do you want to add this number to the total? ")
#     if decision=="y":
#         total=total+num
# print("Your total is:", total)

#43
# direction= input("Please enter a direction: U or D. ")
# if direction =="u":
#     top=int(input("What is the top number?"))
#     for i in range(top+1):
#         print(i)
# elif direction=="d":
#     bottom=int(input("Enter a number below 20."))
#     for i in range(20,(bottom+1),-1):
#         print(i)
# else:
#     print("I don't understand")

#44
num=int(input("How many people are invited to the party? "))

if num>10:
    print("Too many people")
else:
    for i in range(num):
        name=input("What is the ame of your guest?")
        print(name, "has been added to the list")
print("Have a great party!!")
        

