def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

data = [2, 4, 6, 8, 10, 12, 14]
print("array saat ini:", data)

cari = int(input("masukkan angka  yang ingin dicari:  "))

hasil = binary_search(data, cari)

if hasil != -1:
    print("angka di temukan di index:", hasil)

else:
    print("angka tidak ditemukan dalam array.")
