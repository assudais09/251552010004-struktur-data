from collections import deque

class queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return 'Queue kosong!'
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    
    def is_empty(self): return len(self.items) == 0
    def size(self):     return len(self.items)
    def __str__(self):  return str(list(self.items))
    
Q = queue()
Q.enqueue('andi')
Q.enqueue('budi')
Q.enqueue('citra')

print(Q)
print('antrian depan: ', Q.peek())

print('Keluar: ' ,Q.dequeue())
print(Q)
print('sisa antrian: ',Q.size())
print('antrian kosong? ',Q.is_empty())