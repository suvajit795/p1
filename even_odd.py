def check_even_odd(n):
    if n % 2 == 0:
        return f"{n} is even."
    else:
        return f"{n} is odd."

num = int(input("Enter a number: "))
print(check_even_odd(num))
