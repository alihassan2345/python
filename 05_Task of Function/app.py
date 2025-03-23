# Question 01

nums = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
heros = ["superman", "batman", "spiderman", "ironman", "thor", "hulk", "captain america" , "black panther"]
def lenght(list):
    print(len(list))
   

lenght(nums)
lenght(heros)

# Question 02
nums1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
heros1 = ["superman", "batman", "spiderman", "ironman", "thor", "hulk", "captain america" , "black panther"]

def index(list1):
    for i in list1:
        print(i, end=", ")

index(nums1)


# Question 03
def factori():
    num = 5
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(fact)

factori()

# Question 04
def currency():
    pkr = int(input("Enter your amount in pkr : "))
    usd = 295
    print(f"Your amount in USD is : {pkr * usd}")

currency()

# Question 05
def checknum(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
checknum(6)