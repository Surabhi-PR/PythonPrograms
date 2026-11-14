num = int(input("Enter a number :"))
sum, digit = 0, 0
temp = num
while num > 0:
    digit = num % 10
    sum += digit**3
    num //= 10

if sum == temp:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")