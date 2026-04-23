from collections import deque

queue = deque()

queue.append('andi')
queue.append('budi')
queue.append('citra')
queue.append('dina')
deque(['andi' , 'budi' , 'citra' , 'dina'])

print('antrian awal:', list(queue))
print('yang pertama di layani:', queue[0])
print('=== Mulai Melayani ===')

nomor = 1
while queue:
    pelanggan = queue.popleft()
    print(f'[{nomor}] Melayani: {pelanggan}')
    if queue:
        print(f' antrian:{list(queue)}')
    nomor +=1

print ('semua pelanggan telah dilayani!')