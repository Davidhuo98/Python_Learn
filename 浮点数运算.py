import decimal
a=decimal.Decimal('3.141592653')
b=decimal.Decimal('1.234567898')
decimal.getcontext().prec=20
print(a*b)