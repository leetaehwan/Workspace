def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

to_pay = tax_calc(15000000)
pay_tax(to_pay)