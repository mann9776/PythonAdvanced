# for i in range(1, 11):
#     print(f"2 x {i} = {2 * i}")
# This code prints the multiplication table for 2 from 1 to 10.
# for i in "Manmohan":
#     print(i)

# l = [1, 2, 3, 4, 5]
# for i in l:
#     print(i)
# else:
#     print("Loop completed without break")

# l =["Manmohan", "Rohit", "Suresh", "Ramesh", "Sanjay"]
# for name in l:
#     if (name.startswith("S")):
#         print(f"Hello {name}")

# n = int(input("Enter a number: "))
# for i in range(2, n):
#     if (n % i) == 0:
#         print(f"{n} is not a prime number")
#         break
#     else:  
#         print(f"{n} is a prime number")
#         break

product = 1
n = int(input("Enter a number: "))
i = 1
# Calculate the product of all numbers from 1 to n
while (i <= n):
    product *= i
    i += 1
print(f"The factorial of {n} is {product}") 
# product = 0
# n = int(input("Enter a number: "))
# i = 1
# # Calculate the product of all numbers from 1 to n
# while (i <= n):
#     product += i
#     i += 1
# print(f"The product of all numbers from 1 to {n} is {product}") 