
# print(10 > 32 or 10 < 32)

# print(not 10 > 32)

# print(200 > 200 or 200 == 200)


# print(str(True).lower() == "true")


# print(str(True).title() == "True")


# print(len("abc"))



abc = [1, 2, 3, 4, 5]

abc_sq = []

for num in abc:
    new_num = num ** 2
    abc_sq.append(new_num)

# print(abc_sq)

is_even = []
is_odd = []

for num in abc_sq:
    if num % 2 == 0:
        is_even.append(num)
    else:
        is_odd.append(num)

print(is_even)
print(is_odd)

