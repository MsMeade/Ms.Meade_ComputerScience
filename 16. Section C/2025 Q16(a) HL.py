# Question 16 (a)
# Examination Number:
#iii
def get_grade(result):
    grade = "Unsuccessful"

    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    elif result < 40:
        grade = "Unsuccessful"

    return grade

# Calculate and display the mean of a list of results
results = [39,32,62,88,51,62,64,81,77] # Initialise the list
N = len(results) # Initialise N to the number of results
total = 0 # Initialise the running total to 0

# Loop N times
for i in range(N):
    total = total + results[i] # Running total

#i
#ii
# Divide by the total number of results to give the mean
arithmetic_mean = round(total/N,2)

#iv
# Display the answer
print("The mean percentage mark is", arithmetic_mean)

grade=get_grade(arithmetic_mean)
print("The grade for the average result is", grade)

#v

print("The lowest score is",min(results))
print("The highest score is",max(results))

#vi
count1=0
count2=0

for i in range(N):
    if results[i] <40:
        count1=count1+1
    elif results[i]>=50 and i<=79:
        count2=count2+1

print("The number of scores below 40 is",count1)
print("The number of scores between 50 and 79 inclusive is",count2)

#vi
longest_run=[]
current_run=[results[0]]

for i in range(N):
    if results[i]>results[i-1]:
        current_run.append(results[i])
    elif current_run>longest_run:
        longest_run=current_run
        current_run=[results[i]]
        
#print(current_run)
print("The longest run of result increases is",longest_run)






