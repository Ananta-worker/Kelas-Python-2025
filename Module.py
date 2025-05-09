"""
Pengenalan Module
* Module adalah file python yang berisi kumpulan kode python (kelas/fungsi/variable), file python ini memiliki ekstensi
 .py (nama_module.py)
* Package adalah kumpulan dari module-module python dengan tujuan tertentu.
* Kita juga dapat membuat module kita sendiri dengan mengetikkan variable atau fungsi atau kelas di dalam file python.
* Kemudian kita dapat menggunakan module tersebut di kode python yang lain.
"""
from datasumber2 import penjumlahan, pengurangan, perkalian, pembagian
import datasumber

print('Membuat module mengambil data dari file datasumber.py dan datasumber2.py ')
print('-------------------------------------------------------------------------')
print(datasumber.info)
datasumber.sapa_nama('Andi')

penjumlahan(7, 9)
pengurangan(90, 70)
perkalian(5, 5)
pembagian(50, 5)
