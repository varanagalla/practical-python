# mortgage.py
#
# Exercise 1.7
"""
Dave has decided to take out 30-year fixed rate mortgage of $500,000 with Guido's mortgage.
Interest rate is 5% and the monthly payment is $2684.11
Calculate the total amount that Dave will have to pay over the life of the mortgage.

"""
principal = 500000.0
rate = 0.05
monthly_payment = 2684.11
total_paid = 0.0
months_paid = 0
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    principal = principal * (1+rate/12) - monthly_payment
    total_paid += monthly_payment
    months_paid += 1
    if months_paid >= extra_payment_start_month and months_paid <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    total_paid += min(principal, 0)
    principal -= min(principal, 0)
    print(f"{months_paid:>3d} {total_paid:=10.2f} {principal:>10.2f}")

print(f"Total paid: {round(total_paid,2)} over {months_paid} months.")
