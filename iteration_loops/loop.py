my_list = [1, 2, 3, 4, 5, 6]

# for value in my_list:
    # print(value)


# print(value)

# for i in range(1, 50):
#     print(i)


# for x in 10:
#     print(x)

user_1 = {'username': 'rashed', 'id': 1, 'email': 'lelin.rashed784@gmail.com'}
user_2 = {'username': 'lelin', 'id': 2}

my_users = [user_1, user_2]

# for user in my_users:
#     print(user)
#     if "email" in user:
#         print(user['email'])

selected_user = {}
my_user_lookup = 1

for user in my_users:
    if user['id'] == my_user_lookup:
        selected_user = user


print(selected_user)

