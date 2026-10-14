number =input() # takes input from User
sum =0
for i in  number: # for loop used instead of range function to iterate through the input number and store the user input as a string
     sum+=int(i) # Add the digits of the user entered value
     
print("Total Sum:",sum) #print the total sum of the digits of the user entered value