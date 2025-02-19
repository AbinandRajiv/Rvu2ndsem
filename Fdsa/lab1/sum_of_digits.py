def sumofdigit(n):
    if n< 10:
        return n
    else:
        return n%10 + sumofdigit(n/10)

number = int(input("Enter number: "))
digit_sum = sumofdigit(number)
print("Sum of digit of number %d is %d." % (number,digit_sum))
