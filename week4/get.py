# mengakses nilai berdasarkan key

kontak = {'fadhli':'08123456789','andi':'08234567890'}
print('nomor fadhli:',kontak.get('fadhli'))
print('nomor yang tidak ada:',kontak.get('cici','tidak ditemukan'))
