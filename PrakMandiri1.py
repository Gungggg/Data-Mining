import pandas as pd
# Pesan untuk pengguna
print("Memulai proses analisis data...")

# a. Baca dataset menggunakan Pandas
# Pastikan nama file di bawah ini sesuai dengan nama file dataset Anda
nama_file_dataset = 'data_retail.csv'

try:
    df = pd.read_csv(nama_file_dataset)
    print(f"Dataset '{nama_file_dataset}' berhasil dibaca.")
except FileNotFoundError:
    print(f"Error: File '{nama_file_dataset}' tidak ditemukan. Pastikan file ini berada di folder yang sama dengan skrip ini.")
    exit()

# b. Ubah salah satu kolom tanggal ke format datetime
# Mengubah kolom 'First_Transaction' dari format timestamp (milidetik) ke datetime
df['First_Transaction'] = pd.to_datetime(df['First_Transaction'], unit='ms')
print("Kolom 'First_Transaction' berhasil diubah ke format datetime.")

# c. Hitung nilai rata-rata, median, modus untuk salah satu kolom numerik
# Menggunakan kolom 'Average_Transaction_Amount'
rata_rata = df['Average_Transaction_Amount'].mean()
median = df['Average_Transaction_Amount'].median()
modus = df['Average_Transaction_Amount'].mode()[0] # Ambil nilai modus pertama
print("Menghitung statistik (rata-rata, median, modus) untuk 'Average_Transaction_Amount'...")

# d. Kelompokkan data berdasarkan kolom kategorikal, lalu hitung total salah satu kolom numerik
# Mengelompokkan berdasarkan 'Product' dan menghitung total 'Count_Transaction'
pengelompokan = df.groupby('Product')['Count_Transaction'].sum().reset_index()
print("Mengelompokkan data berdasarkan 'Product' dan menghitung total transaksi...")

# e. Simpan hasil pengolahan ke file baru (hasil_praktik_mandiri.xlsx)
# Membuat DataFrame baru untuk menyimpan hasil statistik
hasil_statistik = pd.DataFrame({
    'Metrik': ['Rata-rata Average_Transaction_Amount', 'Median Average_Transaction_Amount', 'Modus Average_Transaction_Amount'],
    'Nilai': [rata_rata, median, modus]
})

# Menyimpan semua hasil ke dalam satu file Excel dengan beberapa sheet
nama_file_hasil = 'hasil_praktik_mandiri.xlsx'
with pd.ExcelWriter(nama_file_hasil) as writer:
    df.to_excel(writer, sheet_name='Data Olahan', index=False)
    hasil_statistik.to_excel(writer, sheet_name='Statistik', index=False)
    pengelompokan.to_excel(writer, sheet_name='Total Transaksi per Produk', index=False)

print("\nAnalisis selesai!")
print(f"Semua hasil telah disimpan di file '{nama_file_hasil}'.")
print("\nRingkasan Hasil:")
print("\n--- Statistik Deskriptif ---")
print(hasil_statistik)
print("\n--- Total Transaksi per Produk ---")
print(pengelompokan.head()) # Menampilkan 5 baris pertama hasil pengelompokan