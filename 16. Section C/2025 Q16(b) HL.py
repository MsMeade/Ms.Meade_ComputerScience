# Question 16(b):
numbers=[1,45,5,4,8,6,7,16]
print("Initial list of values is: ",numbers)
numbers.sort()
print("Sorted list of values is: ",numbers)

length=len(numbers)

if length%2==0:
    num1=numbers[(length)//2]
    num2=numbers[((length)//2)-1]
    median= (num1+num2)/2
    print("The median is",median)

elif length%2==1:
    median=numbers[(length)//2]
    print("The median is",median)
else:
    print("The list is empty. Cannot compute median")

    
