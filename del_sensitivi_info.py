user ={ 'user_name':"deep",
        'password':1123,
        "email":'dff@.com',
        "address":"hyderabad",
        'country':'india'
        }
sen=['password','address','d']
for i in sen:
    if i in user:
        print(f"Deleted key is :{i} and value is :{user[i]}")
        user.pop(i)
    else:
        print(f'{i} is not present,cannot delete\n')
print(f"remaning values are:{user}")