# Nama File: KalenderZettour.py
# Nama/NIM: Bintang Fitra / 24060126140223
# Tanggal: 28 September 2025

# Definisi TanggalZettour
# type TanggalZettour: <hari: int, bulan: int, tahun: int>
type TanggalZettour = tuple[int, int, int]

# Konstruktor
def MakeTanggalZettour(hari: int, bulan: int, tahun: int) -> TanggalZettour:
    return(hari, bulan, tahun)

# Selektor
def hari(TZ: TanggalZettour) -> int:
    return TZ[0]

def bulan(TZ: TanggalZettour) -> int:
    return TZ[1]

def tahun(TZ: TanggalZettour) -> int:
    return TZ[2]

# Fungsi Klasifikasi Tanggal Zettour
def ClassifyZettourDate(TZ: TanggalZettour) -> str:
    if tahun(TZ) % 45 == 0 and hari(TZ) == 17:
        return "Hari Kemenangan"
    elif tahun(TZ) % 4 == 0 and (hari(TZ) % 7 == 0 or hari(TZ) % 30 == 0):
        return "Hari Libur"
    elif tahun(TZ) % 7 != 0 and tahun(TZ) % 99 != 0 and hari(TZ) == 1:
        return "Hari Ibadah"
    elif hari(TZ) % 5 == 0:
        return "Hari Istirahat"
    elif (hari(TZ) + 1) % 5 == 0:
        return "Hari Produktif"
    else:
        return "Hari Biasa"
# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# JANGAN DIUBAH
print(eval(input()))