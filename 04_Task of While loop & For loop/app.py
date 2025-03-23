# Question 01
count = 1 
while count <= 100 : 
    print(count)
    count += 1

# Question 02
count1 = 100
while count1 >= 1 :
    print(count1)
    count1 -= 1

# Question 03
table= int(input("enter your number of multiplication : "))
i =1
condition = int(input("enter your condition : "))
while i <= condition :
    print(f"{table} x {i} = {table * i}")
    i += 1

# Question 04
list1 = [1,4,9,16,25,36,49,64,81,100]
i =0
while i < len(list1) :
    print(list1[i])
    i += 1

# Question 05
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36  
i = 0
while i < len(nums) :
    if (nums[i] == x):   
        print(f"{x} is present in the list")
    i += 1
    
   
# Question 06
forloop = [1,4,9,16,25,36,49,64,81,100]
for i in forloop:
    print(i)

# Question 07
forloop1 = (1,4,9,16,25,36,49,64,81,100,49)
e =0 
x = 49

for i  in  forloop1:
    if (i == x):
        print(f"{i} is present in the list in the index of {e}")
    e +=1
        
# Question 08
for i in range(1,101):
    print(i)

# Question 09
for i in range(100,0 , -1):
    print(i)

# Question 10
table3 = int(input("enter your number of multiplication : "))
condition3 = int(input("enter your condition : "))

for i in range(1,condition3  ):
    print(f"{table3} x {i} = {table3 * i}")

# Question 11
numn = 5
sum = 0
i=1
while i <=5 :
    sum += i
    i += 1
print(sum)

# Question 12
factorial = 100
mul = 1
for i in range(factorial,0,-1): 
    mul *= i
print(mul)