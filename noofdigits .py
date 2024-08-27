n = input("Enter a number")
l = len(n)
if l==0:
    print("Empty string")
elif l>4:
    print("Number greater than 4 digits is not compatible")
else:
    single_digit = ["one","two","three","four","five","six","seven","eight","nine"]
    double_digit = ["","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    power = ["hundred","thousand"]
    
