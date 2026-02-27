User = {'name':'fadhli','age': 27}

# menggunakan get agar aman dari key error
email = User.get('email','Email belum tersedia')
print(email)

# menambahkan ket jika belum ada setdefault
User.setdefault('email','fadhli@example..com')

# update data
User.update({'age':28,'role':'DevOps'})

#menghapus key
age = User.pop('age')

# menampilkan semua key dan values
print(User.keys())
print(User.values())

# menyalin dictionary
user_copy = User.copy()
print(user_copy)

print(User)
print(user_copy)