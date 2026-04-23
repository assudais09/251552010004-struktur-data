import heapq
pq =[]

heapq.heappush(pq, (3, 'task C - Rendah'))
heapq.heappush(pq, (1, 'task C - URGENT'))
heapq.heappush(pq, (3, 'task C - Medium'))

print('priority Queue:' , pq)

while pq:
    prioritas, task = heapq.heappop(pq)
    print(f'[prioritas {prioritas}] proses: {task}')
    