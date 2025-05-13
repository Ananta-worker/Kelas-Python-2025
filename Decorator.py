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
        print(f" ini adalah method ke 2 ")


kucing1 = Kucing()
kucing1.info()

