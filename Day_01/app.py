user = int(input("Enter your number: "))
if user >= 90 and user <= 99.99:
    print("A++")
elif user >= 80 and user <= 89.99:
    print("A+")
elif user >= 70 and user <= 79.99:
    print("A")
elif user >= 60 and user <= 69.99:
    print("B")
elif user >= 50 and user <= 59.99:
    print("C")
elif user >= 40 and user <= 49.99:
    print("D")
else:
    print("Fail")