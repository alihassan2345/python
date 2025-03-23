# Question 1

numbe1 = int(input("enter your number 1 ")) 
number2 = int(input("enter your number 2 "))

print("your sum is : " , numbe1 + number2)

# Question 2

square = int(input("enter your number of square"))

print("your Area is : " , square * square)

# Question 3
flotnumber1 = float(input("enter float number 1 "))
flotnumber2 = float(input("enter float number 2 "))
print("the average of floating number is " , (flotnumber1+flotnumber2)/2)

# Question 4
compare1= int(input("enter 1st comparision"))
compare2= int(input("enter 2nd comparision"))

if compare1 > compare2 :
    print(compare1 , "is greater than " , compare2)
elif compare2 > compare1 :
    print(compare2 , "is greater than " , compare1)

else :
    print(compare1 , "is equal to" , compare2)

# Question 5
user01 = int(input("enter your number 1 : "))
user02 = int(input("enter your number 2 : "))
opreture = input("enter your opreature (+,-,*,/,%) : ")

if opreture == "+":
    print("your result is : " , user01 + user02)

elif opreture == "-":
    print("your result is : " , user01 - user02)

elif opreture == "*":
    print("your result is : " , user01 * user02)

elif opreture == "/":
    if user02 != 0:
        print("your result is : " , user01 / user02)
    else:
        print("Error! Division by zero")
elif opreture == "%":
    if user02 != 0:
        print("your result is : " , user01 % user02)
    else:
        print("Error! Division by zero")
else:
    print("Error! operator is not correct") 

# Question 6    

userinp = int(input("enter your number : "))

if userinp % 2 == 0:
    print(f"your number {userinp} is even")
elif userinp % 2 != 0 :
     print(f"your number {userinp} is odd")

# Question 7
agecheck = int(input("enter your age : "))

if agecheck >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# Question 8
stringlen = input("enter your string ")
lenght =  len(stringlen)
print(f"your string is {stringlen} and its lenght is ",lenght)

# Question 9
P  = float(input("Enter your Principle amount"))
R  = float(input("Enter your Rate of interest"))
T  = float(input("Enter your Time in years"))
SI = (P * R * T) / 100
print("Simple Interest is: ", SI)



