from random import randint, randrange

# 1  - savol


# a = int(randint(-10, 10))
# b = int(randint(-10, 10))
# c = int(randint(-10, 10))
# print("a = ", a, "b = ", b, "c = ", c)
# print(a>0 and b>0 and c<0)
#
# print(b>0 and c>0 and a<0)
#
# print(c>0 and a>0 and b<0)




# 2 - savol
# a = int(randint(0, 10))
# b = int(randint(0, 10))
# print("a = ", a, "b = ", b)
# count = 0
# for i in range(a, b+1):
#     count+=i
# print(f"{a} dan {b} gacha bo`lgan sonlar yig`indisi: {count}")




# 3 - savol

# n = randint(1, 10000)
# print("n = ", n)
# s = str(n)
# print(s[::-1])




# 4 - savol

# n = randint(10, 20)
# a = []
# while len(a)<n:
#     x = randint(5, 15)
#     a.append(x)
# print(a)
# b = []
# for i in range(len(a)):
#     if a[i]%2==0:
#         b.append(a[i])
# print(b)






# 5 - savol

# n = randint(10, 20)
# a = []
# while len(a)<n:
#     x = randint(5, 15)
#     a.append(x)
# print(a)
# min = a[-1]
# for i in range(len(a)-1):
#     if min>a[i]:
#         min = a[i]
#         break
# print(f"{a[-1]} dan birinchi uchragan eng kichkina son: {min}")








# 6 - savol

# s = {1, 2, 3, 4, 5, 6, 78, 12, 34, 45, 56, 67}
#
# s1 = {0, 9, 99, 22, 3, 1, 34, 54, 65, 12, 6}
# print(s.intersection(s1))





# 7 - savol

# n = randint(1, 15)
# print("n = ", n)
# s = {i: i*i+1 for i in range(n+1)}
# #for i in range(n+1):
# #   s[i] = i*i+1
# print("s = ", s)




# 8 -savol

# s = ' viFdubAiN coe Aoeif WonfI '
# count = 0
# n = list(s)
# for i in range(len(n)):
#     if n[i].isupper():
#         count += 1
# print(f"Berilgan matnda {count} ta katta harf bor.")
