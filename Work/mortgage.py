# mortgage.py
mortgage = 500000
rate = 0.05
monthly = 2684.11
total = 0

while mortgage > 0:
    mortgage = mortgage * (1 + rate / 12) - monthly
    total += monthly
    
print("total paid", round(total, 1))
# Exercise 1.7
