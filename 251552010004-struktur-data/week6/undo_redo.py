class textEditor:
    def __init__(self):
        self.content = ''
        self.undo_stack = []

    def write(self, teks):
        self.undo_stack.append(self.content)
        self.content += teks
        print(f'Tulis : {self.content}')

    def undo(self):
        if self.undo_stack:
            self.content = self.undo_stack.pop()
            print(f'UNDO -> {self.content}')
        else:
            print('Tidak bisa undo lagi!')

editor = textEditor()
editor.write('halo')
editor.write('Dunia')
editor.write('!')
editor.undo()
editor.undo()

              