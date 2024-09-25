Monthly_Salary = float(input("Enter the Monthly Salary: "))

if Monthly_Salary >= 30000:
    LoanAmount = float(input("Enter the Loan Amount: "))
    if LoanAmount <= Monthly_Salary*10:
        Months = int(input("Month/s: "))
        Interest = float(LoanAmount * 0.10)
        Final_LoanAmount = LoanAmount + Interest
        Final_Amount = Final_LoanAmount/Months
        MonthlyPayment = print(f"The Monthly Payment is: {Final_Amount:.2f}")
    else:
        print("Too high Loan Request")
else:
    print("Low Salary")