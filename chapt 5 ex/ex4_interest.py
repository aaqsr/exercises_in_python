# formula for interest per annum: ((P*(1+i)^n) - P) P is the principal, i is the annual interest rate, and n is the number of periods

# a

P = float(input("Principal amount?\n$"))
r = float(input("Percentage rate per annum?\n").replace("%",""))
n = float(input("How many years?\n"))

print("When compounded annually, your investment is now: ${0:0.2f}".format((P*(1+(r/100))**n)))
print("When compounded monthly your investment is now: ${0:0.2f}".format(((P*(1+(r/(100*12)))**(n*12)))))
print("When compounded annually your investment is now: ${0:0.2f}".format(((P*(1+(r/(100*365)))**(n*365)))))