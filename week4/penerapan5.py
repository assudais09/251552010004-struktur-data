# database pengguna sederhana

users = {
    'fadhli':'password123',
    'Anya':'admin456',
    'abdu':'dev789'
}

# daftar login yang ingin dicek

login_attempts = [
    
    ('fadhli','password123'),
    ('Anya','admin456'),
    ('abdu','dev789'),
    ('budi','abs123')

]

# cek semua login
for username,password in login_attempts:
    if username in users and users[username] == password:
        print(f'Login {username}:BERHASIL')
    else:
        print(f'Login{username}:GAGAL - Username atau password salah')

        