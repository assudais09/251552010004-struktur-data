class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"Lagu ' {title}' ditambahkan ke playlist.")

    def show_playlist(self):
        current = self.head
        if not current:
            print('Playlisy kosong')
            return
        print('Playlist')

        while current:
            print(f'- {current.title}')
            current = current.next

    def play_all(self):
        current = self.head
        if not current:
            print('Memutar semua lagu:')
            while current:
                print(f'Memutar:{current.title}')
                current = current.next

playlist = Playlist()
playlist.add_song("Lagu A - Aku")
playlist.add_song('Lagu B - bersamamu')
playlist.add_song('Lagu C - kita')

print()
playlist.show_playlist()

print()
playlist.play_all()