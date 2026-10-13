n = int(input())# get the input from user
result=0 # I want to store the sum of even numbers in this variable 
# using for loop to iterate through the range of numbers from 0 to n
for i in range(0,n+1):
    if i % 2== 0 : # condition to check if number is Even or not 
         result+=i
print("Sum:" , result)