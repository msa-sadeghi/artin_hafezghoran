# numbers = [1,2,3,4,5,6]
# for x in numbers:
#     if x % 2 == 0:
#         print(f"first even number is {x}")
#         break
#     print(f"{x} is odd")

# for i in range(1, 11):# 1, 2,3, ... , 10
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")

print("main menu")

# while True:
#     print("1 => greet")
#     print("2 => bye")
#     print("3 => exit")
#     choice = input("\n enter your choice: ")
#     if choice == "1":
#         name = input("enter your name: ")
#         print("hello", name)
#     elif choice == "2":
#         name = input("enter your name: ")
#         print("bye", name)
#     elif choice == "3":
#         print("see you again")
#         break
#     else:
#         print("invalid input")
#         continue

# try:
#     x = int(input("enter a number: "))
#     y = int(input("enter a number: "))

#     print(x / y)
# except ValueError:
#     print("invalid number")
# except ZeroDivisionError:
#     print("can not divide by zero")

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i * j}")
#     print()

# rows = 5
# for i in range(1, rows + 1):
#     print("*" * i)

# for i in range(1, rows + 1):
#     spaces = " " * (rows - i)
#     stars = "* " * i
#     print(spaces + stars)


# x = int(input("enter a number"))
# for num in range(2, x):
#     is_prime = True
#     for d in range(2, num):
#         if num % d == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num} is prime")


a = 0
b = 1
for i in range(100):
    temp = a
    a = b
    b = temp + b
print(a)
