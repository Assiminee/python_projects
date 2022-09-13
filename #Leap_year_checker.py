#Leap_year_checker
year=int(input("What year are you testing for?\n"))
if (year%4==0):
    #The code tests the first line, if it is true it moves on to the second condition.
    if (year%100==0):
        #If the second condition is true, it will once again move on to the third condition.
        if(year%400==0):
            #if the third and final condition is again correct, it will print the following statement
            print("Leap year.")
        else:
            #if the third condition is false, meaning that that the second one is true, it will print this statement
            print("Not leap year.")
    else: 
        #If the first condition is true but the second isn't, then the following statement will be printed
        print("Leap year.")
else:
    #If none of the conditions are true, the following statement will be printed
    print("Not leap year.")
#It's important to note that the conditional statements must have an alterative output if they are incorrect. Otherwise, in some cases, each condition will print its output. 2000 for example.
#Therefore, there should be else statements that are triggered in case a condition is false/true.

    