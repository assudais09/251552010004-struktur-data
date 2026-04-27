class node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = node('A')
b = node('B')
c = node('C')

a.next = b 
b.next = c

current = a
while current:
    print(f'node @{id(current)} data : {current.data} next: {id(current.next)if current.next else None}')
    current = current.next