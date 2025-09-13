# mortgage.py
mortgage = 500000
rate = 0.05
monthly = 2684.11
total = 0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while mortgage > 0:
    months += 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        mortgage = mortgage * (1 + rate / 12) - (monthly + extra_payment)
    else:
        mortgage = mortgage * (1 + rate / 12) - monthly
    total += monthly

    if mortgage < 0:
        total += mortgage
        mortgage = 0

    print(f"{months} {round(total, 2)} {round(mortgage, 2)}")
    
print(f"total paid {round(total, 2)}")
print(f"number of months {months}")
# Exercise 1.7
