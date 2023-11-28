# -----------------------------------------------------------------------
# FA 23 CMPSC 360 Extra Credit Assignment
# Base Conversion
# 
# Name: Souradeep Bhattacharya
# ID: skb6381@psu.edu
# 
# 
# -----------------------------------------------------------------------

def base_conversion(number: int, base: int) -> int:
    # CHECK
    # -- Base Check
    if base < 2 or base > 9:
        return ("Invalid Base")

    list1 = [*str(number)]
    digits = [int(i)for i in list1]
    # -- Digits Check
    accum = 0
    for d in digits:
        if d in range(0, base):
            accum += 1
        elif d not in range(0, base):
            accum -= 999

    if accum < 0:
        return ("The input is wrong. Digits should be less than the base.")

    # CALCULATION
    # -- When Base is correct and Digits are correct
    digits.reverse()
    digits_reverse = {}
    for i in range(len(digits)):
        digits_reverse[i] = digits[i]
    
    converted = []
    for a,b in digits_reverse.items():
        x = b*(base**(a))
        converted.append(x)

    value = 0
    for c in converted:
        value +=c

    return value


if __name__ == '__main__':
    print("BASE CONVERSION TO Base_10")
    number = int(input('Enter the number: '))
    base = int(input('Enter the base: '))
    BC = (base_conversion(number, base))
    print(BC)
