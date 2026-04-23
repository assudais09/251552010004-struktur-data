stack = []
print('awal :' ,stack)

# stack.append('a')
stack.append('b')
stack.append('c')
print('setelah push: ',stack)

top = stack[-1]
print('peek :',top)

popped = stack.pop()
print('Dipop : ',popped)
print('Stack : ',stack)

print('kosong? ', len(stack)==0)
print('ukuran: ', len(stack))