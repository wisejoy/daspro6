# Input ordo matriks A
baris_A = int(input("Masukkan jumlah baris matriks A: "))
kolom_A = int(input("Masukkan jumlah kolom matriks A: "))

matriks_A = []

# Input elemen matriks A
print("Masukkan elemen matriks A:")
for i in range(baris_A):
    baris_matriks = []
    
    for j in range(kolom_A):
        angka = int(input(f"A[{i}][{j}]: "))
        baris_matriks.append(angka)
        
    matriks_A.append(baris_matriks)

# Input ordo matriks B
baris_B = int(input("Masukkan jumlah baris matriks B: "))
kolom_B = int(input("Masukkan jumlah kolom matriks B: "))

matriks_B = []

# Input elemen matriks B
print("Masukkan elemen matriks B:")
for i in range(baris_B):
    baris_matriks = []
    
    for j in range(kolom_B):
        angka = int(input(f"B[{i}][{j}]: "))
        baris_matriks.append(angka)
        
    matriks_B.append(baris_matriks)

# Menampilkan matriks A
print("\nMatriks A:")
for i in range(baris_A):
    print(matriks_A[i])

# Menampilkan matriks B
print("\nMatriks B:")
for i in range(baris_B):
    print(matriks_B[i])

# Mencek kesesuaian ordo
if kolom_A != baris_B:
    print("\nPerkalian matriks tidak dapat dilakukan.")
    print("Jumlah kolom A harus sama dengan jumlah baris B.")
else:
    # Membuat matriks hasil
    hasil = []
    
    for i in range(baris_A):
        baris_hasil = []
        
        for j in range(kolom_B):
            jumlah = 0
            
            for k in range(kolom_A):
                jumlah = jumlah + matriks_A[i][k] * matriks_B[k][j]
                
            baris_hasil.append(jumlah)
            
        hasil.append(baris_hasil)
        
    # Menampilkan hasil
    print("\nHasil perkalian matriks:")
    for i in range(baris_A):
        print(hasil[i])