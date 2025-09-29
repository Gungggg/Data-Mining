# Impor library pandas yang diperlukan untuk membaca dan menganalisis data
import pandas as pd

# Nama file CSV Anda
nama_file = 'BMW_sales_data_2010_2024.csv'

try:
    # Membaca file CSV ke dalam sebuah DataFrame
    df = pd.read_csv(nama_file)

    # --- Menghitung Statistik untuk Kolom 'Price_USD' ---

    # 1. Menghitung Mean (Rata-rata)
    mean_harga = df['Price_USD'].mean()

    # 2. Menghitung Median (Nilai Tengah)
    median_harga = df['Price_USD'].median()

    # 3. Menghitung Modus (Nilai yang Paling Sering Muncul)
    #    .mode() dapat mengembalikan lebih dari satu nilai jika ada, jadi kita ambil yang pertama [0]
    modus_harga = df['Price_USD'].mode()[0]


    # --- Menampilkan Hasil ---

    print(f"Analisis Statistik untuk Kolom 'Price_USD' dari file {nama_file}:")
    print("-" * 60)
    # Tampilkan hasil dengan format yang mudah dibaca
    print(f"Mean (Rata-rata Harga): ${mean_harga:,.2f}")
    print(f"Median (Harga Tengah): ${median_harga:,.2f}")
    print(f"Modus (Harga Paling Sering Muncul): ${modus_harga:,.2f}")
    print("-" * 60)

except FileNotFoundError:
    print(f"Error: File tidak ditemukan!")
    print(f"Pastikan file dengan nama '{nama_file}' sudah ada di direktori yang sama.")
except KeyError:
    print("Error: Kolom 'Price_USD' tidak ditemukan dalam file.")
    print("Mohon periksa kembali nama kolom pada file CSV Anda.")