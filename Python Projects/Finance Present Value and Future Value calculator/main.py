print("What are you trying to calculate?")
print()
print("1. Future Value")
print("2. Present Value")
print("3. Interest Rate")
print("2. Number of years")

userChoice = input("Pick a number: ")

match userChoice:
    case "1":
        print("You chose future value, Give me the following:")
        print()
        presentValue = input("Present value(no commas): ")
        interestRate = input("Interest rate (Write it as a decimal e.g'0.25'): ")
        numbOfYears  = input("Number of years invested: ")

        presentValue =  float(presentValue)
        interestRate =  float(interestRate)
        numbOfYears  =  float(numbOfYears)

        futureValue =  presentValue * ((1 + interestRate) ** numbOfYears)
        print(f"Your future value is: {futureValue:.2f}")

    case "2":
        print("You chose present value, Give me the following:")
        print()
        futureValue  = input("Future value(no commas): ")
        interestRate = input("Interest rate (Write it as a decimal e.g'0.25'): ")
        numbOfYears  = input("Number of years invested: ")

        futureValue  = float(futureValue)
        interestRate = float(interestRate)
        numbOfYears  = float(numbOfYears)

        presentValue = futureValue / ((1 + interestRate) ** numbOfYears)
        print(f"Your present value is: {presentValue:.2f}")

    case "3":
        print("You chose interest rate, Give me the following:")
        print()
        futureValue = input("Future value(no commas): ")
        presentValue = input("Present value(no commas): ")
        numbOfYears = input("Number of years invested: ")

        futureValue = float(futureValue)
        presentValue = float(presentValue)
        numbOfYears = float(numbOfYears)

        interestRate = (futureValue / presentValue) ** (1 / numbOfYears) - 1
        interestRate = interestRate * 100
        print(f"Your interest value is: {interestRate:.2f} %")




