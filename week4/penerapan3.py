# database pengguna sederhana

users = {
    'fadhli':'password123',
    'Anya':'admin456',
    'budi':'dev789'
}

# login check
username = 'fadhli'
password = 'password12'

if username in users and users[username] == password:
    print('Login berhasil')

else:
    print('Username atau password salah')
