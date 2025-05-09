"""
Built-in variable pada module
* Di dalam module terdapat beberapa built-in variable yang bisa kita panggil.
* Built-in variable ini menggunakan pola double underscore (dunder), mirip seperti magic method dalam class.
Macam-macam built-in variable:
* __name__=berisi nama module dalam bentuk string. Jika module adalah program utama, maka namanya akan
  menjadi "__main__".
* __doc__=berisi module docstring.
* __file__=berisi module file path/direktorinya.
"""

import datasumber

# nama module:__main__ : file utama
print(__name__)
# menuliskan variable/keterangan
print(__doc__)
# mengembalikan lokasi file
print(__file__)

print('---------------')
print(datasumber.__name__)
print(datasumber.__doc__)
print(datasumber.__file__)