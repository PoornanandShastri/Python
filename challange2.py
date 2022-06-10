input1 = input('Would you like to continue? ')

#print("Would you like to continue?")
#input1=input()

if input1 == 'no' or input1== 'n':
    print("Exiting")
elif input1 == 'yes' or input1 == 'y':
    print("Continuing ...  \nComplete!")
else:
    print("Please try again and respond with yes or no.")