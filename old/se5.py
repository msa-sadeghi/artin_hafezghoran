# username = input("enter the username: ")
# password = input("enter the password: ")

# if username == "admin":
#     if password == "1234":
#         print(f"Welcome {username}")
#     else:
#         print(f"{username}, your password is not correct")
# else:
#     print("username is not correct")


# count = 1
# while count <= 5:
#     print(f"iteration # {count}")
#     count += 1

# n = int(input("enter a number: "))
# i = 1
# t = 0
# while i <= n:
#     t += i
#     i += 1
# print(t)

# import random

# secret = random.randint(1, 10)
# attempts = 0

# while True:
#     guess = int(input("enter a number between 1 - 10: "))
#     attempts += 1
#     if guess == secret:
#         print(f"great after {attempts} attempts you guessed the secret")
#         break
#     elif guess < secret:
#         print(f"your guess is less than the secret")
#     else:
#         print(f"your guess is greater than the secret")


# import random
# colors = ["red", "green", "blue"]
# print(random.choice(colors))
# print(random.choices(colors, k=2))

# text = "python"
# for ch in text:
#     print(ch)

# fruits = ["banana",  "apple"]
# for item in fruits:
#     print(item)


# range(n) — از 0 تا n-1
# for i in range(5):
#     print(i, end=" ")    # 0 1 2 3 4

# # range(start, stop)
# for i in range(1, 6):
#     print(i, end=" ")    # 1 2 3 4 5

# # range با گام
# for i in range(0, 11, 2):
#     print(i, end=" ")    # 0 2 4 6 8 10

# # شمارش معکوس
# for i in range(5, 0, -1):
#     print(i, end=" ")    # 5 4 3 2 1


# print("python", end="\t")
# print("javascript", end="\t")

count = int(input("how many numbers:  "))
total = 0
maximum = None
minimum = None

for i in range(count):
    num = int(input(f"number {i+1}: "))
    total += num
    if maximum is None or num > maximum:
        maximum = num
    if minimum is None or num < minimum:
        minimum = num

print(f"\n=== result ===")
print(f"sum:   {total}")
print(f"average: {total/count:.2f}")
print(f"max: {maximum}")
print(f"min:  {minimum}")
