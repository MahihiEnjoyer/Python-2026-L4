#1:
pi = 3.1415
radius = float(input("Enter circle radius? "))
area = radius**2 *pi
print("Circle area =", area)

#2:
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = celsius * 1.8 + 32
print(f"{float(celsius)}(C) = {float(fahrenheit)} (F)")

#3:
num = int(input("Enter a number? "))

if num < 2:
    print(num, "is a NOT prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is a NOT prime number")

#4:
num = int(input("Enter a number? "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is a NOT perfect number")

#5:
colors = ["Blue", "Yellow", "Red", "Purple", "Orange"]

favorite_color = input("What is your favorite color? ")

if favorite_color in colors:
    index = colors.index(favorite_color)
    print("Your color is at index", index, "in my list")
else:
    print("Sorry, I could not find your color")

#6:
range1 = range(0, 7)
print(*range1)

range2 = range(1, 11, 3)
print(*range2)

range3 = range(5, 0, -1)
print(*range3)

range4 = range(6, -3, -2)
print(*range4)

#7:
def remove_dollar_sign(s):
    return s.replace("$", "")

print(remove_dollar_sign("$100"))

#8:
def extract_even(l):
    even_numbers = []

    for num in l:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

print(extract_even([1, 4, 5, -1, 10]))

#9:
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))

#10:
def get_divisors(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors

print(get_divisors(12))





