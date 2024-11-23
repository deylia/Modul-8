# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:17:36 2024

@author: Dewi aulia nurjanah
065002400010
"""

def jumlah_rekursif(angka):
    if not angka:
        return 0
    return angka[0] + jumlah_rekursif(angka[1:])

jumlah = float(input("Masukkan Jumlah: "))

# Ubah jumlah menjadi integer untuk menentukan jumlah iterasi
jumlah = int(jumlah)

angka = []
for i in range(1, jumlah + 1):
    num = float(input(f"Masukkan bilangan ke-{i}: "))
    angka.append(num)

hasil = jumlah_rekursif(angka)
print(f"Hasil dari penjumlahan adalah: {hasil}")