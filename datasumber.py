"ini file sapa"

info = "Ini di dalam module datasumber.py"


def sapa_nama(nama):
    print(f'Halo {nama}')


if __name__ == "__main__":
    print('ini adalah modul utama')
else:
    print('ini di dalam datasumber.py sebagai module import')