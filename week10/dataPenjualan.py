import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan selama 6 hari pertama (10 baris)

data =[
    {"Tanggal": "2025-07-01", "Warna": "merah", "ukuran": "M", "jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-01", "Warna": "putih", "ukuran": "L", "jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-02", "Warna": "hitam", "ukuran": "XL", "jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-03", "Warna": "merah", "ukuran": "S", "jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-04", "Warna": "putih", "ukuran": "M", "jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-04", "Warna": "hitam", "ukuran": "L", "jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-05", "Warna": "merah", "ukuran": "XL", "jumlah": 1, "Harga": 35000},
    {"Tanggal": "2025-07-05", "Warna": "putih", "ukuran": "S", "jumlah": 3, "Harga": 20000},
    {"Tanggal": "2025-07-06", "Warna": "hitam", "ukuran": "S", "jumlah": 2, "Harga": 20000},
    {"Tanggal": "2025-07-06", "Warna": "merah", "ukuran": "L", "jumlah": 3, "Harga": 30000}
]

df = pd.DataFrame(data)
df["Total"] = df["jumlah"] * df["Harga"]

total_penjualan = df["Total"].sum()

warna_order = ["merah", "putih", "hitam"]
warna_terjual = df.groupby("Warna")["jumlah"].sum().reindex(warna_order)
total_kaos = warna_terjual.sum()

probabilitas = (warna_terjual / total_kaos) * 100

print("Total penjualan selama 6 hari: Rp {:,.0f}".format(total_penjualan))
print("\nProbabilitas warna paling sering dibeli:")

for warna, prob in probabilitas.items():
    print(f"{warna}: {prob:.2f}%")

warna_grafik = ["red", "white", "black"]
plt.figure(figsize=(8, 5))
plt.bar(probabilitas.index, probabilitas.values, color=warna_grafik, edgecolor='gray')
plt.title("probabilitas pembelian kaos per warna (6 hari)")
plt.ylabel("persentase (%)")
plt.xlabel("Warna")
plt.ylim(0, 50)
plt.xticks(rotation = 0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

warna_data = list(zip(warna_terjual.index, warna_terjual.values))

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

sorted_data = bubble_sort(warna_data)

print("\nHasil pengurutan (bubble Sort) Berdasarkan jumlah terbanyak:")
for warna, jumlah in sorted_data:
    print(f"{warna}: {jumlah} kaos")

plt.figure(figsize=(8, 5))
sorted_warna, sorted_jumlah = zip(*sorted_data)
warna_grafik_sorted = ["red" if w == "merah" else "white" if w == "putih" else "black" for w in sorted_warna]

plt.bar(sorted_warna, sorted_jumlah, color=warna_grafik_sorted, edgecolor="gray")
plt.title("hasil buble sort: warna kaos paling banyak terjual")
plt.ylabel("jumlah kaso")
plt.xlabel("warna")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()