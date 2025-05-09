"""
Generator
* Generator adalah objek yang mirip seperti objek iterable.
* Perbedaanya generator tidak memiliki elemen secara langsung seperti objek iterable.
* Untuk mengakses elemen generator, kita perlu memanggilnya satu persatu.
* Generator lebih efisien dalam menggunakan memori.
* Fungsi generator menggunakan keyword yield yang mengembalikan nilai satu per satu.
* Contoh sintak generator
def fungsi_gen(n):
    #blok kode
        yield nilai_gen
        yield nilai_gen, dst.
"""


def simple_gen():
    yield 1
    yield 2
    yield 3
    yield 4


simple_gen()
for item in simple_gen():
    print(item)

# built-in function next()
simple_gen_var = simple_gen()
print(next(simple_gen_var))
print(next(simple_gen_var))
print(next(simple_gen_var))
print(next(simple_gen_var))


def simple_gen(n):  # range(5): 0,1,2,3,4
    for i in range(n):
        yield i


gen1 = simple_gen(10)   # objek generator dipanggil dengan pengulangan
for item in gen1:
    print(item)

obj_iter = [1, 2, 3, 4]    # object iterator bisa langsung dipanggil
print(obj_iter)

gen1 = simple_gen(10)   # gen1 di deklarasi ulang, nilai di reset
print(list(gen1))       # di rubah menjadi tipe list
print('---------')
gen1 = simple_gen(10)   # gen1 di deklarasi ulang, nilai di reset
print(tuple(gen1))      # di rubah menjadi tipe tuple


def simple_gen(n):
    for i in range(n):
        yield i**2      # nilai i bisa di sesuaikan kebutuhan


gen1 = simple_gen(21)
print(list(gen1))


def is_prima(num):      # bil prima adalah bil yang hanya bisa dibagi 1 dan bil itu sendiri
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prima(4))      # cek bil prima ditampilkan


def prima_gen(n):
    # fungsi mengecek bil prima
    def is_prima1(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in range(2, n+1):
        if is_prima1(i):
            yield i


prima1 = prima_gen(20)
for item in prima1:
    print(item)

file = open('contoh.txt', mode='r')
for item in file:
    print(item)
file.close()

# filter kata dalam text
print("membuat fungsi filter text\n")


def filter_text(file, kata_filter):
    with open(file, mode='r') as file:
        for item in file:
            if kata_filter in item:
                yield item


filter1 = filter_text("contoh.txt", "proyek")   # mencari kata "proyek"
for item in filter1:
    print(item)

# filter kata dalam text pakai next
print("membuat fungsi filter text pakai next\n")

filter2 = filter_text("contoh.txt", "Python")   # mencari kata "Python"
print(next(filter2))                            # dieksekusi perbaris perbaris
print(next(filter2))
print(next(filter2))

file.close()