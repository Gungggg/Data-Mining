import pandas as pd
import numpy as np

try:
    dataset = pd.read_csv('data_retail.csv', sep=',')

    print("--- Dataset Berhasil Dibaca ---")

    # Menampilkan 5 baris pertama
    print("\nLima baris pertama:")
    print(dataset.head()) 

    # Menampilkan 5 baris terakhir
    print("\nLima baris terakhir:")
    print(dataset.tail())

    # Menampilkan jumlah total baris dan kolom
    print("\nJumlah total baris dan kolom:")
    print(dataset.shape)
    
    # Mengubah kolom dari Unix timestamp (milidetik) ke Datetime
    dataset['First_Transaction'] = pd.to_datetime(dataset['First_Transaction'], unit='ms')
    dataset['Last_Transaction'] = pd.to_datetime(dataset['Last_Transaction'], unit='ms')

    print("Konversi Tanggal Berhasil!")
    print("\nLima baris pertama dengan format tanggal baru:")
    print(dataset.head())
    
    print("\nTipe data kolom:")
    print(dataset.info())

    pd.set_option('display.max_column', 20)

    #Mengimpor library datetime
    import datetime

    #Mengubah kolom First_Transaction dan Last_Transaction ke bentuk Datetime
    dataset['First_Transaction']=pd.to_datetime(dataset['First_Transaction']/1000, unit='s', origin='1970-01-01').dt.date
    dataset['Last_Transaction'] =pd.to_datetime(dataset['Last_Transaction']/1000, unit='s', origin='1970-01-01').dt.date

    #Mengurutkan data berdasarkan tanggal transaksi pertama
    dataset.sort_values('First_Transaction', inplace=True)

    #Menampilkan isi data
    print(dataset)

except FileNotFoundError:
    print("Sistem masih tidak dapat menemukan file. Mohon coba unggah ulang.")
except Exception as e:
    print(f"Terjadi error: {e}")