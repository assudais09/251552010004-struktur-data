# database pengguna sederhana

users = {
    'fadhli':'password123',
    'Anya':'admin456',
    'budi':'dev789'
}

print('=== Loginn Manual ===')
input_username = input('Masukkan username:')
input_password = input('Masukkan password:')

if input_username in users and users[input_username] == input_password:
    print(f'Login {input_username}:BERHASIL')
else:
    print(f'Login{input_username}: GAGAL - Username atau password salah')
