# 1. Impor library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

# Nama file CSV Anda
# Pastikan file ini ada di folder yang sama dengan script Python Anda
nama_file = 'BMW_sales_data_2010_2024.csv'

try:
    # 2. Baca data dari file CSV dan masukkan ke dalam variabel bernama 'df'
    # Inilah bagian yang hilang dari kode Anda sebelumnya
    df = pd.read_csv(nama_file)

    # 3. Sekarang variabel 'df' sudah ada, kita bisa membuat histogram
    print("Membuat histogram dari kolom 'Price_USD'...")
    plt.figure(figsize=(10, 6)) # Mengatur ukuran gambar agar lebih jelas
    plt.hist(df['Price_USD'], bins=30, edgecolor='black', alpha=0.7)
    
    # Menambahkan judul dan label agar grafik mudah dibaca
    plt.title('Distribusi Harga Mobil BMW')
    plt.xlabel('Harga (USD)')
    plt.ylabel('Frekuensi (Jumlah Mobil)')
    plt.grid(True)

    # 4. Tampilkan histogram yang sudah dibuat
    plt.show()

except FileNotFoundError:
    print(f"Error: File '{nama_file}' tidak ditemukan. Mohon periksa kembali nama dan lokasi file.")
except KeyError:
    print("Error: Kolom 'Price_USD' tidak ditemukan di dalam file. Periksa nama kolomnya.")