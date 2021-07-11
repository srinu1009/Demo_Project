num = int(input("Enter the number to find its factorial: "))
factorial = 1

while num >= 1:
    factorial = factorial * num
    num = num - 1

print(factorial)

