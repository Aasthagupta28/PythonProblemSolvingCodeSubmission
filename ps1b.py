#Problem Set 1b
#Name: Aastha Gupta
#Time spent: 4:30
balance = float(input('enter the balance on your credit card:'))
annual_interest_rate=float(input('enter the annual credit card interest rate as a decimal:'))

minmum_monthly_payment=.08*balance
balance=balance
while balance>=0:
    month=1
    minmum_monthly_payment=minmum_monthly_payment+500
    balance=balance

    while month<=12 and balance>0:
        month=month+1
        monthly_interest_rate=annual_interest_rate/12.0
        balance=balance*(1+monthly_interest_rate)-minmum_monthly_payment
print("RESULT")
print("Monthly payment to pay off debt in 1 year:",minmum_monthly_payment)
print("Number of months needed:",month)
print("Balance:",balance)
        
