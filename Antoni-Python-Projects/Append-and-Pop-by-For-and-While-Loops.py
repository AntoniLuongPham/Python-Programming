# init empty list
one_to_ten = []


x = 10
y = 0

# append by for loop
for _ in range(x):
    y += 1
    one_to_ten.append(y)
    print(one_to_ten)

# pop by for loop
for _ in range(x):
    if one_to_ten != []:
        one_to_ten.pop()
        print(one_to_ten)

# append by while loop
i = 0
while i < 10:
    i += 1
    one_to_ten.append(i)
    print(one_to_ten)

# pop by while loop
i = 0
while i < 10 and one_to_ten != []:
    i += 1
    one_to_ten.pop(i - 10)
    print(one_to_ten)
