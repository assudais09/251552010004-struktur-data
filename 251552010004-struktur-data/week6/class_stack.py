class lemari:
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return ' stack kosong!'
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
def main():
    l = lemari()
    # l.push('baju')
    # l.push('celana')
    # l.push('jaket')
    print(l)

    print('elemen atas :',l.peek())
    print('hapus elemen :',l.pop())
    print(l)
    print('jumlah akhir elemen :',l.size())
    print('kosong ?',l.is_empty())

main()
