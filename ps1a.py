#Problem set 1a
#Name: Aastha Gupta
#Time Spent: 5 hours


balance = float(input("Enter the balance on the credit card"))
annual_interest_rate = float(input ("Enter the annual interest rate"))
minimum_monthly_payment = float(input("Enter the minimum monthly payment rate"))
for month in range(1,13):
    minimum_monthly_payment= round(( minimum_monthly_payment*balance),2)
    interest_paid = round(((annual_interest_rate/12)*balance), 2)
    principal_paid = round(( minimum_monthly_payment - interest_paid),2)
    remaining_balance = round(( balance- principal_paid),2)
    balance = remaining_balance
    month +=1
    print (("Minmimum monthly payment ") + str(minimum_monthly_payment))
    print (("Principal Paid ") + str(principal_paid))
    print (("Remaining Balance ") + str(remaining_balance))
    print ( ("Month")+str (month))
    print (("Remaining Balance")+ str(balance))
