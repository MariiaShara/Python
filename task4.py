n=int(input("Enter an integral positive number: "))
max=0
while(n>10):
    d = n % 10
    n = n // 10
    if d > max:
        max=d
print(f"The maximum digit in the number is: {max}")

