kontak = {'Fadhli':'08123456789'}
print('sebelum set default:',kontak)

kontak.setdefault('andi','08234567890')
kontak.setdefault('Fadhli','0900000000')
print('setelah set default:',kontak)