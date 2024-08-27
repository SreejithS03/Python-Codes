num =int(input("Enter a decimal number"))
binary = bin(num)
octal = oct(num)
hexa = hex(num)
print(f" Binary value : {binary.replace("0b", "")}")
print(f" Octal value : {octal.replace("0o", "")}")
print(f" hexadecimal value : {hexa.replace("0x","")}")

