"""
- Menggunakan decorator untuk memberikan otoritas
- class Abstact (bagian dari OOP)
    - Salah satu penggunaan decorator adalah dalam membuat class abstract.
    - Kalau class adalah blueprint/rancangan dari sebuah objek.
    - Maka class Abstract adalah rancangan dari sebuah class.
    Product dari class abstact adalah class
    - class abstract menggunakan module abc (abstract base class).
    - dimana dari module abc kita akan menggunakan superclass yang namanya abc dan
      decorator yang namanya abstactmethode.
    - sintaknya
    class NamaKelas(ABC):
       @abstractmethod
       def method()
          pass
"""
from abc import ABC, abstractmethod     # impor untuk class abstract


Hesti = {"nama": "Hesti", "role": "user1"}
Ansar = {"nama": "Ansar", "role": "user2"}
Alex = {"nama": "Alex", "role": "user3"}
Darwis = {"nama": "Darwis", "role": "user4"}


def otoritas(admin):
    def decorator(fungsi):
        def wrapper(user_admin, user_umum):
            if user_admin["role"] == admin:
                fungsi(user_admin, user_umum)
            else:
                print(f'{user_admin["nama"]} tidak memiliki otoritas')
        return wrapper
    return decorator


@otoritas("user2")
def menghapus_user(user_admin, user_umum):
    print(f'{user_admin["nama"]} menghapus {user_umum["nama"]}')


menghapus_user(Ansar, Hesti)
menghapus_user(Hesti, Ansar)

# class Abstact


class Hewan(ABC):
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def info2(self):
        pass


class Kucing(Hewan):
    def info(self):
        print("\nini adalah kelas kucing")

    def info2(self):
        print(f"\nini adalah method ke 2 ")


kucing1 = Kucing()
kucing1.info()


class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        luas = self.sisi * self.sisi
        return luas

    def keliling(self):
        kel = self.sisi * 4
        return kel

    def __str__(self):
        return str(self.sisi)


persegi1 = Persegi(6)
print(f"luas persegi dengan sisi= {persegi1} cm: ")
print(persegi1.luas())

print("keliling persegi: ")
print(f"keliling persegi dengan sisi= {persegi1} cm: ")
print(persegi1.keliling())


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        luas = self.panjang * self.lebar
        return luas

    def keliling(self):
        kel = self.panjang * 2 + self.lebar * 2
        return kel

    def __str__(self):
        return f"Panjang: {self.panjang} cm, Lebar: {self.lebar} cm"


persegipanjang1 = PersegiPanjang(6, 5)

print(f"Luas persegi panjang dengan {persegipanjang1}: {persegipanjang1.luas()} cm²")
print(f"Keliling persegi panjang dengan: {persegipanjang1}: {persegipanjang1.keliling()} cm")
