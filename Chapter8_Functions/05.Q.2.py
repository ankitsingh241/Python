# Convert celcius to farenheit.

def farh(cel):
    return ((cel*(9/5)) + 32)

c = int(input("Enter a temp.: "))
f = farh(c)

print(f"{c} degree celcius is equal to {f} degree farenheit.")

