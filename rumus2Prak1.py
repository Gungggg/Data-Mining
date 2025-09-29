import pandas as pd

# Nama file CSV Anda
nama_file = 'BMW_sales_data_2010_2024.csv'

try:
    # Baca file CSV ke dalam DataFrame
    df = pd.read_csv(nama_file)

    # --- 1. Hitung Statistik Awal (Sebelum Dihapus) ---
    print("--- Statistik Awal (Sebelum Penghapusan) ---")
    mean_sebelum = df['Price_USD'].mean()
    median_sebelum = df['Price_USD'].median()
    modus_sebelum = df['Price_USD'].mode()[0]
    
    print(f"Mean (Rata-rata)   : ${mean_sebelum:,.2f}")
    print(f"Median (Nilai Tengah): ${median_sebelum:,.2f}")
    print(f"Modus (Nilai Umum)   : ${modus_sebelum:,.2f}\n")

    # --- 2. Hapus 5% Data dengan Nilai Tertinggi ---
    
    # Cari nilai ambang batas (quantile 0.95 atau persentil ke-95)
    # Semua data di atas nilai ini dianggap sebagai 5% teratas.
    ambang_batas_atas = df['Price_USD'].quantile(0.95)
    
    print(f"Menghapus data dengan harga di atas: ${ambang_batas_atas:,.2f} (Ambang Batas 5% Teratas)")

    # Buat DataFrame baru yang hanya berisi data di bawah atau sama dengan ambang batas
    df_setelah = df[df['Price_USD'] <= ambang_batas_atas]
    
    # --- 3. Hitung Ulang Statistik (Setelah Dihapus) ---
    print("\n--- Statistik Baru (Setelah Penghapusan) ---")
    mean_setelah = df_setelah['Price_USD'].mean()
    median_setelah = df_setelah['Price_USD'].median()
    modus_setelah = df_setelah['Price_USD'].mode()[0]
    
    print(f"Mean (Rata-rata)   : ${mean_setelah:,.2f}")
    print(f"Median (Nilai Tengah): ${median_setelah:,.2f}")
    print(f"Modus (Nilai Umum)   : ${modus_setelah:,.2f}\n")

    # --- 4. Tampilkan Perbandingan ---
    print("--- Perbandingan Perubahan ---")
    print(f"Penurunan Mean   : ${mean_sebelum - mean_setelah:,.2f}")
    print(f"Penurunan Median : ${median_sebelum - median_setelah:,.2f}")
    print(f"Perubahan Modus  : ${modus_sebelum - modus_setelah:,.2f}")

except FileNotFoundError:
    print(f"Error: File '{nama_file}' tidak ditemukan. Mohon periksa kembali nama dan lokasi file.")
except KeyError:
    print("Error: Kolom 'Price_USD' tidak ditemukan di dalam file. Periksa nama kolomnya.")
except Exception as e:
    print(f"Terjadi error: {e}")